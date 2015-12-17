import copy
import datetime
import numbers
import six

from .config import DefaultConfig
from .locales import LOCALES
from .parser import InnerTagField, VariableField, SwitchField, PyslateException


class Pyslate(object):
    """
    Main class responsible for all the translation and localization. When constructed it's necessary to set language,
    backend. It's possible to set custom config, context dict and instance of cache class.
    """

    def __init__(self, language, backend=None, config=DefaultConfig(), context=None,
                 cache=None, locales=None, parser=None, on_missing_tag_key_callback=None):
        """
        Constructor

        :param language: see language field
        :param backend: see backend field
        :param config: see config field
        :param context: see context field
        :param cache: see cache field
        :param locales: this dict extends default dict of locales available in :obj:`locales.LOCALES <pyslate.pyslate.locales.LOCALES>`
        :param parser: see parser field
        :param on_missing_tag_key_callback: see on_missing_tag_key_callback field
        :return: object of Pyslate class
        """

        self.config = config
        """
        Object having the same fields as config.DefaultConfig class, which specifies all configurable parameters
        """

        self.language = language
        """
        Language used by an instance of Pyslate as a main language.
        """

        if backend is None:
            raise AssertionError("no pyslate backend is specified")
        self.backend = backend
        """
        Backend object is responsible for supplying values of tags for specified key and language
        from a persistent storage. It doesn't make any further processing nor doesn't interpret data.
        """

        self.cache = cache
        """
        Object responsible for caching. It must implement the same methods as cache.SimpleMemoryCache.
        If cache is not needed, then it can be None.
        Even if specified, cache may not be used when ``config.ALLOW_CACHE`` is False.
        """

        self.locales = copy.deepcopy(LOCALES)
        """
        Dict containing information about locales available in the application.
        It stores information like native language name, date and time format, decimal separator and
        rules for plural forms available in this language.
        Keyword argument `locales` does extend, not replace the default set of locales.
        Locales specified in keyword argument takes higher precedence over default locales.
        For examples of correct locale specification see :obj:`pyslate.locales.LOCALES`
        """
        if locales:
            self.locales = dict(self.locales, **locales)

        self.fallbacks = {}
        """
        Dict containing language fallbacks. e.g. dict ``{"pl": "en"}`` means
        'when tag requested for "pl" is not available, then use a tag value for language "en"'
        """

        self.global_fallback = config.GLOBAL_FALLBACK_LANGUAGE
        """
        Global fallback is a language which is used when tag is not available for a main language nor for language's fallback language.
        It's assumed that tag's base (variant-less) value for global_fallback is ALWAYS available.
        """

        self._decorators = {}

        self._functions = {}

        # dictionary storing info whether function/decorator is being deterministic and their cache
        # are shared between functions and decorators
        self.functions_deterministic = {}
        """
        A dictionary where key is a name of function or a decorator and value is True/False.
        True means the function is deterministic for the same set of arguments and its result should be cached to be reused.
        It makes sense to set it to True only if a function/decorator is going to be often used with the same arguments
        and function processing is expensive.
        """
        self.functions_memory = {}
        """
        A dictionary used as cache for deterministic functions and decorators.
        Key is a function/decorator name and value is a tuple containing a pair:
        list of input arguments, result. It's discouraged to access it manually except clearing it.
        """

        # load default available decorators
        for decorator_name in config.GLOBAL_DECORATORS:
            self.register_decorator(decorator_name, config.GLOBAL_DECORATORS[decorator_name])
        for language in config.LANGUAGE_SPECIFIC_DECORATORS:
            decorators_for_language = config.LANGUAGE_SPECIFIC_DECORATORS[language]
            for decorator_name in decorators_for_language:
                self.register_decorator(decorator_name, decorators_for_language[decorator_name], language=language)

        self.parser = parser if parser else config.PARSER_CLASS()
        """
        Object responsible for parsing the tag value string to get Abstract Syntax Tree to support
        variable, inner tag and switch fields. Default implementation is a pure-python PLY parser.
        """

        if context is None:  # handle default value
            context = {}
        self.context = context
        """
        Contains dict whose key-value pairs are values automatically appended to kwargs argument
        of the :obj:`translate` method. They can later be used in variable or switch fields.
        It's good to specify kwargs which need to be available globally, e.g. information about the person reading the text.
        """

        if not on_missing_tag_key_callback:
            on_missing_tag_key_callback = config.ON_MISSING_TAG_KEY
        self.on_missing_tag_key_callback = on_missing_tag_key_callback
        """
        Contains two-parameter function which is run when some tag value cannot be got from the backend.
        It should return string which is written to the output instead of the missing tag.
        The first parameter is tag key, the second is dict of interpolable parameters (a.k.a. kwargs).
        You can replace it with your own implementation having some side-effect, for example logging of the missing tags.
        """

    def translate(self, tag_name, **kwargs):
        """
        Method returning fully translated tag value for a specified tag_name using kwargs as a list of keyword arguments.
        If there's no tag value for specified language, then tag value for fallback language
        (or global fallback language) is used.

        :param tag_name: tag key which should be translated. It can contain decorators
        :param kwargs: arguments which can be interpolated into tag value
        :return: translated value for specified tag key.
        """
        # treat main specified tag as inner tag
        tag_name = "${" + tag_name + "}"

        # parse it to get tag key, remove (unnecessary) id and take its decorators
        inner_tag_node = self.parser.parse(tag_name)[0]
        tag_name = inner_tag_node.contents[0]

        t9n = self._translate(tag_name, **kwargs)[0]

        for decorator_name in inner_tag_node.decorators:
            t9n = self._call_decorator(decorator_name, t9n)

        return t9n

    def _translate(self, tag_name, **kwargs):

        kwargs = dict(self.context, **kwargs)  # add context variables, which have lower priority

        if "number" in kwargs:
            number_variant = self._first_left_value_from(self.locales, self._get_languages())["number_rule"](
                kwargs["number"])

            base_variant_parts = tag_name.partition("#")
            tag_name = base_variant_parts[0] + "#" + number_variant + base_variant_parts[2]

            if tag_name[-1] == "#":
                tag_name = tag_name[:-1]

        tag_base = tag_name.partition("#")[0]
        variant = tag_name.partition("#")[2]
        kwargs["tag_v"] = variant

        if tag_base in self._functions:
            function_language = self._first_left_key_from(self._functions[tag_base], self._get_languages())
            if (self.functions_deterministic[tag_base]  # deterministic function so maybe result is already known
                and tuple([function_language] + sorted(kwargs.items())) in self.functions_memory[tag_name]):
                t9n, form = self.functions_memory[tag_name][tuple([function_language] + sorted(kwargs.items()))]
            else:
                helper = PyslateHelper(self)
                function_for_language = self._first_left_value_from(self._functions[tag_base], self._get_languages())

                t9n = function_for_language(helper, tag_name, kwargs)
                form = helper.returned_form
                if self.functions_deterministic[tag_base]:
                    self.functions_memory[tag_name][tuple([function_language] + sorted(kwargs.items()))] = (t9n, form)
        else:
            t9n, form = self._get_raw_content(tag_name, kwargs), self._get_raw_form(tag_name)

        nodes = self.parser.parse(t9n)

        t9n = self._traverse(nodes, kwargs)

        return t9n, form

    @staticmethod
    def _first_left_value_from(dictionary, keys):
        for key in keys:
            if key in dictionary:
                return dictionary[key]
        return None

    @staticmethod
    def _first_left_key_from(dictionary, keys):
        for key in keys:
            if key in dictionary:
                return key
        return None

    def localize(self, value, short=False):
        """
        Method returning localized string representation of a value specified in the argument.
        Currently it guarantees to correctly localize the following types:
        float, datetime.date, datetime.datetime, datetime.time
        If value cannot be localized then its string representation is returned.

        :param value: value to be localized
        :return: string representation of the value, localized if being instance of the supported types
        """
        locale_data = self._first_left_value_from(self.locales, self._get_languages())
        if not self.config.LOCALE_FORMAT_NUMBERS:
            return str(value)
        if isinstance(value, float):
            return self._format_float(value, locale_data["format"]["decimal_point"])
        if isinstance(value, numbers.Integral):
            return str(value)
        if isinstance(value, datetime.datetime):
            format_field = "datetime_short" if short else "datetime"
            return value.strftime(locale_data["format"][format_field])
        if isinstance(value, datetime.date):
            format_field = "date_short" if short else "date"
            return value.strftime(locale_data["format"][format_field])
        if isinstance(value, datetime.time):
            format_field = "time_short" if short else "time"
            return value.strftime(locale_data["format"][format_field])
        else:
            return str(value)

    def _format_float(self, n, decimal_point):
        formatted_float = "{:.3f}".format(n).rstrip("0").rstrip(".")
        if decimal_point != ".":
            formatted_float = formatted_float.replace(".", decimal_point)
        return formatted_float

    t = translate
    "Alias for :obj:`translate`"

    l = localize
    "Alias for :obj:`localize`"

    def register_decorator(self, decorator_name, function, is_deterministic=False, language=None):
        """
        Registers a new decorator which will be available in the translation system.
        Overwrites any other decorator or function with the same name.

        :param decorator_name: name of the decorator available in the translation system
        :param function: a function whose only argument is input string string and returns an altered string
        :param is_deterministic: if True then return value of the decorator for specified arguments will be cached
               to be reused in the future. Keep it disabled unless you really know you need it.
        :param language: language for which decorator will be available, If unspecified then it's available for all languages

        """
        if decorator_name in self._functions:
            del self._functions[decorator_name]

        if not language:
            language = self.global_fallback

        if decorator_name not in self._decorators:  # no such decorator for any language yet, so create a dict for it
            self._decorators[decorator_name] = {}
        self._decorators[decorator_name][language] = function

        self.functions_deterministic[decorator_name] = is_deterministic
        self.functions_memory[decorator_name] = {}

    def register_function(self, tag_name, function, is_deterministic=False, language=None):
        """
        Registers a new custom function which will be available in the translation system.
        Overwrites any other decorator or function with the same name.

        :param tag_name: name base tag key for which the function is accessible in an inner tag field. See the examples.
        :param function: function with 3 arguments:
            - a helper (instance of PyslateHelper), which is a facade for translating specified tags or setting grammatical form of the custom function
            - tag_name
            - params (keyword arguments specified in Pyslate.translate)

        :param is_deterministic: if True then return value and grammatical form of the function for specified arguments
               will be cached to be reused in the future. Keep it disabled unless you really know you need it.
        :param language: language for which function will be available. If unspecified then it's available for all languages

        """
        if tag_name in self._decorators:
            del self._decorators[tag_name]

        if not language:
            language = self.global_fallback

        if tag_name not in self._functions:  # no such function for any language yet, so create a dict for it
            self._functions[tag_name] = {}
        self._functions[tag_name][language] = function

        self.functions_deterministic[tag_name] = is_deterministic
        self.functions_memory[tag_name] = {}

    def _get_raw_content(self, tag_name, kwargs):
        """Gets and returns content from backend considering all possible tag and language fallbacks"""

        requested_tags = [tag_name]
        if "#" in tag_name:
            tag_and_variant = tag_name.partition("#")
            for i in range(len(tag_and_variant[2]) - 1, 0, -1):
                requested_tags += [tag_and_variant[0] + tag_and_variant[1] + tag_and_variant[2][:i]]
            requested_tags += [tag_and_variant[0]]

        if self.cache and self.config.ALLOW_CACHE:
            cached_content = self.cache.load(requested_tags[0], self._get_languages()[0])
            if cached_content is not None:
                return cached_content

        retrieved_content = self.backend.get_content(requested_tags, self._get_languages())
        if retrieved_content is None:
            retrieved_content = self.on_missing_tag_key_callback(requested_tags[0], kwargs)
        elif self.cache and self.config.ALLOW_CACHE:
            self.cache.save(tag_name, self.language, retrieved_content)
        return retrieved_content

    def _get_languages(self):
        languages = [self.language]
        if self.language in self.fallbacks:
            languages += [self.fallbacks[self.language]]
        languages += [self.global_fallback]
        return languages

    def _get_raw_form(self, tag_name):
        """Returns grammatical form got from backend considering all possible tag and language fallbacks
        Returns none if no form is set"""
        requested_tags = [tag_name]
        if "#" in tag_name:
            requested_tags += [tag_name.partition("#")[0]]

        languages = self._get_languages()
        return self.backend.get_form(requested_tags, languages)

    def _traverse(self, nodes, kwargs):
        nodes_after_replacing_inner_tags = []
        forms_by_id = {}
        for node in nodes:
            text, form_by_id_dict = self._replace_inner_tag_or_pass(node, kwargs)
            nodes_after_replacing_inner_tags.append(text)
            forms_by_id.update(form_by_id_dict)

        fully_interpreted_nodes = []
        for node in nodes_after_replacing_inner_tags:
            fully_interpreted_nodes.append(self._interpolate_variable_or_switch_field(node, kwargs, forms_by_id))

        return "".join(fully_interpreted_nodes)

    def _replace_inner_tag_or_pass(self, node, kwargs):
        if not isinstance(node, InnerTagField):  # do nothing
            return node, {}

        tag_name = self._traverse(node.contents, kwargs)

        if not self.config.ALLOW_INNER_TAGS:  # when inner tags are disabled then print them as-is
            return "${" + tag_name + "}", {}
        final_kwargs = kwargs

        if node.tag_id:  # if this inner tag has a string ID, like that: ${ID:some_value}
            if "groups" in kwargs:
                final_kwargs = dict(kwargs)
                del final_kwargs["groups"]
                # available kwargs can be overwritten by elements of dict, which is a group specific for this tag's id
                final_kwargs.update(kwargs["groups"][node.tag_id])

        text, form = self._translate(tag_name, **final_kwargs)

        for decorator_name in node.decorators:
            text = self._call_decorator(decorator_name, text)

        if not node.tag_id:
            return text, {}
        return text, {node.tag_id: form}

    def _interpolate_variable_or_switch_field(self, node, kwargs, forms):
        if isinstance(node, six.string_types):  # just return the string
            return node
        elif isinstance(node, VariableField):
            return self._replace_variable_fields(node, kwargs)
        elif isinstance(node, SwitchField):
            if not self.config.ALLOW_SWITCH_FIELDS:
                return ""
            return self._replace_switch_fields(node, kwargs, forms)
        else:
            raise PyslateException("invalid node: {} of type {} in parsed text".format(node, type(node)))

    def _replace_variable_fields(self, node, kwargs):
        if node.contents not in kwargs and node.contents not in self.context:
            return self.config.ON_MISSING_VARIABLE(node.contents)

        value = ""
        if node.contents in kwargs:
            value = kwargs[node.contents]
        elif node.contents in self.context:
            value = kwargs[node.contents]

        for decorator_name in node.decorators:
            value = self._call_decorator(decorator_name, value)

        if isinstance(value, float):
            value = self.localize(value)

        return str(value)

    def _replace_switch_fields(self, node, kwargs, forms):
        param_name = "variant"
        if node.tag_id:
            param_name = node.tag_id

        if param_name in kwargs and self._contained_in(kwargs[param_name], node.cases) is not False:
            return self._contained_in(kwargs[param_name], node.cases)
        elif param_name in forms and self._contained_in(forms[param_name], node.cases) is not False:
            return self._contained_in(forms[param_name], node.cases)
        else:
            return node.cases[node.first_key]

    def _call_decorator(self, decorator_name, value):
        try:
            decorator_language = self._first_left_key_from(self._decorators[decorator_name], self._get_languages())

            if (self.functions_deterministic[decorator_name]  # deterministic function so maybe result is already known
                and tuple([decorator_language, value]) in self.functions_memory[decorator_name]):
                return self.functions_memory[decorator_name][tuple([decorator_language, value])]

            decorator = self._decorators[decorator_name][decorator_language]
            return decorator(value)
        except KeyError:
            raise PyslateException("No decorator with name '{}' for main language or any of its fallbacks {}".
                                   format(decorator_name, self._get_languages()))

    def _contained_in(self, param, cases):
        for case_key in cases.keys():
            if case_key in param:
                return cases[case_key]
        return False


class PyslateHelper(object):
    """
    Class given as a first argument of the custom functions. It's a facade which allows for translating
    or getting a grammatical form for specified tag keys. It also allows for setting a grammatical form of an entity
    represented by this custom function. This way a custom function can be a black-box treated exactly the same as
    a normal inner tag field.
    """

    def __init__(self, pyslate):
        self.pyslate = pyslate
        self.returned_form = None

    def translation(self, tag_name, **kwargs):
        """
        Returns a translated string for specified tag_name and kwargs. Delegates to Pyslate.translate method.
        """
        return self.pyslate._translate(tag_name, **kwargs)[0]

    def form(self, tag_name, **kwargs):
        """
        Returns grammatical form of the tag_name tag (which can be None).
        """
        return self.pyslate._translate(tag_name)[1]

    def translation_and_form(self, tag_name, **kwargs):
        """
        If you need both translation and grammatical form, then it's more efficient to use it to get both at once.
        Returns a tuple whose first element is a translated string for specified tag_name and kwargs.
        The second element is grammatical form of the tag (which can be None).

        """
        return self.pyslate._translate(tag_name, **kwargs)

    def return_form(self, form):
        """
        Specifies grammatical form of the entity represented by the custom function.
        It can later be retrieved by other fields of the tag value.

        :param form: grammatical form of this custom function
        """
        self.returned_form = form

    def get_suffix(self, tag_name):
        if "#" in tag_name:
            return tag_name.partition("#")[2]
        return ""

    def pass_the_suffix(self, tag_name):
        if self.get_suffix(tag_name):
            return "#" + self.get_suffix(tag_name)
        return ""

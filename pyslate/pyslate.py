from collections import namedtuple
import datetime
from pyslate.config import DefaultConfig
from pyslate.locales import LOCALES
from pyslate.parser import InnerTagField, VariableField, SwitchField, PyslateException
import numbers


class Pyslate:

    def __init__(self, language, backend=None, config=DefaultConfig(), context=None, cache=None):
        self.config = config

        self.language = language
        self.backend = backend if backend else self.config.BACKEND_CLASS()
        config.ALLOW_CACHE = cache is not None or config.ALLOW_CACHE
        self.cache = cache if cache else (config.CACHE_CLASS() if self.config.ALLOW_CACHE else None)
        self.fallbacks = {}
        self.global_fallback = config.GLOBAL_FALLBACK_LANGUAGE

        self.decorators = {}
        self.functions = {}

        # info about being deterministic and memory for pure functions is common for decorators and functions
        self.functions_deterministic = {}
        self.functions_memory = {}

        self.parser = config.PARSER_CLASS()

        if context is None: # handle default value
            context = {}

        self.context = context

    def translate(self, tag_name, **kwargs):
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

        if "number" in kwargs and not (self.config.DISABLE_NUMBER_FOR_TAG_KEYS_WITH_VARIANT and "#" in tag_name):
            fallback = self._first_left_value_from(LOCALES, self._get_languages())["number_rule"](kwargs["number"])
            tag_name = tag_name.partition("#")[0] + "#" + fallback

        tag_base = tag_name.partition("#")[0]
        variant = tag_name.partition("#")[2]
        kwargs["tag_v"] = variant

        if tag_base in self.functions:
            if (self.functions_deterministic[tag_base]  # deterministic function so maybe result is already known
                    and tuple(sorted(kwargs.items())) in self.functions_memory[tag_name]):
                t9n, form = self.functions_memory[tag_name][tuple(sorted(kwargs.items()))]
            else:
                helper = PyslateHelper(self)
                t9n = self.functions[tag_base](helper, tag_name, kwargs)
                form = helper.returned_form
                if self.functions_deterministic[tag_base]:
                    self.functions_memory[tag_name][tuple(sorted(kwargs.items()))] = (t9n, form)
        else:
            t9n, form = self._get_raw_content(tag_name), self._get_raw_form(tag_name)

        nodes = self.parser.parse(t9n)

        t9n = self.traverse(nodes, kwargs)

        return t9n, form

    def _first_left_value_from(self, dictionary, keys):
        for key in keys:
            if key in dictionary:
                return dictionary[key]
        return None

    def localize(self, value):
        if not self.config.LOCALE_FORMAT_NUMBERS:
            return str(value)
        if isinstance(value, float):
            locale_data = self._first_left_value_from(LOCALES, self._get_languages())
            return self._format_float(value, locale_data["format"]["decimal_point"])
        if isinstance(value, numbers.Integral):
            return str(value)
        if isinstance(value, datetime.datetime):
            return str(value)
        if isinstance(value, datetime.date):
            return str(value)
        if isinstance(value, datetime.time):  # todo
            return str(value)
        else:
            return str(value)

    def _format_float(self, n, decimal_point):
        formatted_float = "{:.3f}".format(n).rstrip("0").rstrip(".")
        if decimal_point != ".":
            formatted_float = formatted_float.replace(".", decimal_point)
        return formatted_float

    t = translate
    l = localize

    def set_fallback_language(self, base_language, fallback_language):
        self.fallbacks[base_language] = fallback_language

    def set_global_fallback(self, fallback_language):
        self.global_fallback = fallback_language

    def set_context(self, context):
        self.context = context

    def append_to_context(self, **kwargs):
        self.context.update(kwargs)

    def register_decorator(self, decorator_name, function, is_deterministic=False):
        if decorator_name in self.functions:
            del self.functions[decorator_name]
        self.decorators[decorator_name] = function
        self.functions_deterministic[decorator_name] = is_deterministic
        self.functions_memory[decorator_name] = {}

    def register_function(self, tag_name, function, is_deterministic=False):
        if tag_name in self.decorators:
            del self.functions[tag_name]
        self.functions[tag_name] = function
        self.functions_deterministic[tag_name] = is_deterministic
        self.functions_memory[tag_name] = {}

    def _get_raw_content(self, tag_name):
        """Gets and returns content from backend considering all possible tag and language fallbacks"""

        requested_tags = [tag_name]
        if "#" in tag_name:
            requested_tags += [tag_name.partition("#")[0]]

        if self.config.ALLOW_CACHE:
            cached_content = self.cache.load(requested_tags[0], self._get_languages()[0])
            if cached_content is not None:
                return cached_content

        retrieved_content = self.backend.get_content(requested_tags, self._get_languages())
        if retrieved_content is None:
            retrieved_content = "[MISSING TAG '{0}']".format(requested_tags[0])
        elif self.config.ALLOW_CACHE:
            self.cache.save(tag_name, self.language, retrieved_content)
        return retrieved_content

    def _get_languages(self):
        languages = [self.language]
        if self.language in self.fallbacks:
            languages += [self.fallbacks[self.language]]
        languages += [self.global_fallback]
        return languages

    def _get_raw_form(self, tag_name):
        """Gets and returns grammatical form from backend considering all possible tag and language fallbacks
        Returns none if no form is set"""
        requested_tags = [tag_name]
        if "#" in tag_name:
            requested_tags += [tag_name.partition("#")[0]]

        languages = self._get_languages()
        return self.backend.get_form(requested_tags, languages)

    def traverse(self, nodes, kwargs):
        nodes_with_inner = []
        forms = {}
        for node in nodes:
            text, form = self._replace_inner_tag_or_pass(node, kwargs)
            nodes_with_inner.append(text)
            forms.update(form)
        nodes = [self._replace_variable_or_switch_field(node, kwargs, forms) for node in nodes_with_inner]
        return "".join(nodes)

    def _replace_inner_tag_or_pass(self, node, kwargs):
        if type(node) is not InnerTagField:  # do nothing
            return node, {}
        tag_name = self.traverse(node.contents, kwargs)
        if not self.config.ALLOW_INNER_TAGS:  # when inner tags are disabled then print them as-is
            return "${" + tag_name + "}", {}
        final_kwargs = kwargs

        if node.tag_id:
            if "groups" in kwargs:
                final_kwargs = dict(kwargs)
                del final_kwargs["groups"]
                final_kwargs.update(kwargs["groups"][node.tag_id])

        text, form = self._translate(tag_name, **final_kwargs)

        for decorator_name in node.decorators:
            text = self._call_decorator(decorator_name, text)

        if not node.tag_id:
            return text, {}
        return text, {node.tag_id: form}

    def _replace_variable_or_switch_field(self, node, kwargs, forms):
        if type(node) is str:  # just return the string
            return node
        elif type(node) is VariableField:
            return self._replace_variable_fields(node, kwargs)
        elif type(node) is SwitchField:
            if not self.config.ALLOW_SWITCH_FIELDS:
                return ""
            return self._replace_switch_fields(node, kwargs, forms)
        else:
            raise PyslateException("invalid node: " + str(type(node)) + " in parsed text")

    def _replace_variable_fields(self, node, kwargs):
        if node.contents not in kwargs and node.contents not in self.context:
            return "[MISSING VALUE FOR '{0}']".format(node.contents)

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

        if param_name in kwargs and kwargs[param_name] in node.cases:
            return node.cases[kwargs[param_name]]
        elif param_name in forms and forms[param_name] in node.cases:
            return node.cases[forms[param_name]]
        else:
            return node.cases[node.first_key]

    def _call_decorator(self, decorator_name, value):
        decorator = self.decorators[decorator_name]
        return decorator(value)


class PyslateHelper:

    def __init__(self, pyslate):
        self.pyslate = pyslate
        self.returned_form = None

    def translation(self, tag_name):
        return self.pyslate._get_raw_content(tag_name)

    def translation_and_form(self, tag_name):
        return self.translation(tag_name), self.form(tag_name)

    def form(self, tag_name):
        return self.pyslate._get_raw_form(tag_name)

    def return_form(self, form):
        self.returned_form = form




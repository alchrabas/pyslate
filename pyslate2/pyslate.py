from pyslate2.config import PyslateConfig
from pyslate2.locales import LOCALES
from pyslate2.parser import InnerTag, Placeholder, Variants


class Pyslate:

    def __init__(self, language, backend=None, config=PyslateConfig()):
        self.config = config

        self.language = language
        self.backend = backend if backend else self.config.BACKEND_CLASS()
        self.fallbacks = {}
        self.global_fallback = "en"
        self.functions = {}
        self.parser = config.PARSER_CLASS()

    def translate(self, tag_name, **kwargs):

        if "number" in kwargs and not (self.config.DISABLE_NUMBER_FOR_VARIANT_TAGS and "#" in tag_name):
            languages = self._get_languages() + [self.config.NUMBER_FALLBACK_LANGUAGE]
            fallback = self._first_left_value(LOCALES, languages)["number_rule"](kwargs["number"])
            tag_name = tag_name.partition("#")[0] + "#" + fallback

        kwargs["tag_v"] = tag_name.partition("#")[2]

        if tag_name in self.functions:
            t9n = self.functions[tag_name](self, tag_name, kwargs)
        else:
            t9n = self._get_raw_content(tag_name)

        nodes = self.parser.parse(t9n)
        print(nodes)
        t9n = "".join([self.traverse(node, kwargs) for node in nodes])

        return t9n

    def _first_left_value(self, dictionary, keys):
        for key in keys:
            if key in dictionary:
                return dictionary[key]
        return None

    def localize(self, value):
        if not self.config.LOCALE_FORMAT_NUMBERS:
            return value
        if isinstance(value, float):
            locale_data = self._first_left_value(LOCALES, self._get_languages())
            return locale_data["format"]["float"](value)

    t = translate
    l = localize

    def set_fallback_language(self, base_language, fallback_language):
        self.fallbacks[base_language] = fallback_language

    def set_global_fallback(self, fallback_language):
        self.global_fallback = fallback_language

    def _get_languages(self):
        languages = [self.language]
        if self.language in self.fallbacks:
            languages += [self.fallbacks[self.language]]
        languages += [self.global_fallback]
        return languages

    def register_function(self, tag_name, function):
        self.functions[tag_name] = function

    def _get_raw_content(self, tag_name):
        """Gets and returns content from backend considering all possible tag and language fallbacks"""

        requested_tags = [tag_name]
        if "#" in tag_name:
            requested_tags += [tag_name.partition("#")[0]]

        languages = self._get_languages()

        ee = self.backend.get_content(requested_tags, languages)
        if ee is None:
            ee = "[MISSING TAG '{0}']".format(requested_tags[0])
        return ee

    def _get_raw_grammar(self, tag_name):
        """Gets and returns grammar from backend considering all possible tag and language fallbacks
        Returns none if no grammar is set"""
        requested_tags = [tag_name]
        if "#" in tag_name:
            requested_tags += [tag_name.partition("#")[0]]

        languages = self._get_languages()
        return self.backend.get_grammar(requested_tags, languages)

    def traverse(self, node, kwargs):
        if type(node) is InnerTag:
            tag_name = "".join([self.traverse(child, kwargs) for child in node.contents])
            final_kwargs = kwargs

            if node.tag_id:
                if "groups" in kwargs:
                    final_kwargs = dict(kwargs)
                    del final_kwargs["groups"]
                    final_kwargs.update(kwargs["groups"][node.tag_id])
            return self.translate(tag_name, **final_kwargs)
        elif type(node) is Placeholder:
            return self._replace_placeholder(node, kwargs)
        elif type(node) is Variants:
            return self._replace_variants(node, kwargs)
        elif type(node) is str:
            return node

    def _replace_placeholder(self, node, kwargs):
        if node.contents in kwargs:
            value = kwargs[node.contents]
            if isinstance(value, float):
                value = self.localize(value)
            return str(value)
        return "[MISSING VALUE FOR '{0}']".format(node.contents)

    def _replace_variants(self, node, kwargs):
        param_name = "variant"
        if node.tag_id:
            param_name = node.tag_id

        if param_name in kwargs and kwargs[param_name] in node.variants:
            return node.variants[kwargs[param_name]]
        else:
            return node.variants[node.first_key]

    class Tag():

        def __init__(self, name):
            self.name = name


class PyslateHelper:

    def __init__(self, pyslate):
        self.pyslate = pyslate

    def translation(self, tag_name):
        pass

    def translation_and_grammar(self, tag_name):
        pass

    def grammar(self, tag_name):
        pass






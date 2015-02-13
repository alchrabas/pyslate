from pyslate2 import config
from pyslate2.parser import InnerTag, Placeholder, Variants


class Pyslate:

    def __init__(self, language, backend=config.BACKEND_CLASS()):
        self.language = language
        self.backend = backend
        self.fallbacks = {}
        self.global_fallback = "en"
        self.functions = {}
        self.parser = config.PARSER_CLASS()

    def translate(self, tag_name, **kwargs):

        if "number" in kwargs and not (config.DISABLE_NUMBER_FOR_VARIANT_TAGS and "#" in tag_name):
            languages = self._get_languages() + [config.NUMBER_FALLBACK_LANGUAGE]
            fallback = self._first_left_value(config.NUMBERS, languages)(kwargs["number"])
            tag_name = tag_name.partition("#")[0] + "#" + fallback


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

    def localize(self):
        pass

    t = translate
    l = localize

    def set_fallback_language(self, base_language, fallback_language):
        self.fallbacks[base_language] = fallback_language

    def set_global_fallback(self, fallback_language):
        self.global_fallback = fallback_language

    def _get_languages(self):
        languages = [self.language]
        if self.fallbacks[self.language]:
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
        return self.backend.get_content(requested_tags, languages)

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
        return str(kwargs[node.contents]) if node.contents in kwargs else "MISSING TAG '{0}'".format(node.contents)

    def _replace_variants(self, node, kwargs):
        param_name = "variant"
        if node.tag_id:
            param_name = node.tag_id

        if param_name in kwargs and kwargs[param_name] in node.variants:
            return node.variants[kwargs[param_name]]
        else:
            return node.variants[node.first_key]


class PyslateHelper:

    def __init__(self, pyslate):
        self.pyslate = pyslate

    def translation(self, tag_name):
        pass

    def translation_and_grammar(self, tag_name):
        pass

    def grammar(self, tag_name):
        pass






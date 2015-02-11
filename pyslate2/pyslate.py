import string
from pyslate2 import config
from pyslate2.parser import InnerTag, Placeholder


class Pyslate:

    def __init__(self, language, backend=config.BACKEND_CLASS()):
        self.language = language
        self.backend = backend
        self.fallbacks = {}
        self.global_fallback = "en"
        self.functions = {}
        self.parser = config.PARSER_CLASS()

    def translate(self, tag_name, **kwargs):

        if tag_name in self.functions:
            return self.functions[tag_name](self, tag_name, kwargs)

        if "number" in kwargs and not (config.DISABLE_NUMBER_FOR_VARIANT_TAGS and "#" in tag_name):
            tag_name = tag_name.partition("#")[0] + "#" + config.NUMBERS[self.language](kwargs["number"])

        t9n = self._get_raw_content(tag_name)

        nodes = self.parser.parse(t9n)
        print(nodes)
        t9n = "".join([self.traverse(node, kwargs) for node in nodes])

        return t9n

    def localize(self):
        pass

    t = translate
    l = localize

    def set_fallback_language(self, base_language, fallback_language):
        self.fallbacks[base_language] = fallback_language

    def set_global_fallback(self, fallback_language):
        self.global_fallback = fallback_language

    def get_fallbacks(self):
        fallbacks = []
        if self.fallbacks[self.language]:
            fallbacks += [self.fallbacks[self.language]]
        fallbacks += [self.global_fallback]
        return fallbacks

    def register_function(self, tag_name, function):
        self.functions[tag_name] = function

    def _get_raw_content(self, tag_name):
        """Gets and returns content from backend considering all possible tag and language fallbacks"""

        requested_tags = [tag_name]
        if "#" in tag_name:
            requested_tags += [tag_name.partition("#")[0]]

        languages = [self.language] + self.get_fallbacks()

        return self.backend.get_content(requested_tags, languages)

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
            return self.replacement(node, kwargs)
        elif type(node) is str:
            return node

    def replacement(self, node, kwargs):
        return str(kwargs[node.contents]) if node.contents in kwargs else "MISSING TAG '{0}'".format(node.contents)


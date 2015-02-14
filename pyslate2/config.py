__author__ = 'aleksander chrabaszcz'

from pyslate2.backend import PyslateJsonBackend
from pyslate2.parser import PyParser

class PyslateConfig:

    def __init__(self):
        # global fallback
        self.BASE_LANGAUGE = "en"

        self.FALLBACKS = {
            "pl": "en",
        }

        self.ALLOW_RECURSIVE_TAGS = True

        self.BACKEND_CLASS = PyslateJsonBackend

        self.ALLOW_CACHE = False
        self.CACHE_CLASS = None

        self.PARSER_CLASS = PyParser

        self.ALLOW_SPECIAL_TAGS = {
            "NUMBER": True,
        }

        self.DISABLE_NUMBER_FOR_VARIANT_TAGS = False

        self.NUMBER_FALLBACK_LANGUAGE = "en"

        self.ALLOW_GRAMMAR_VARIANTS = True

        self.LOCALE_FORMAT_NUMBERS = True
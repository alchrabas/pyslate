__author__ = 'aleksander chrabaszcz'

from pyslate2.backend import PyslateJsonBackend
from pyslate2.parser import PyParser

# global fallback
BASE_LANGAUGE = "en"

ALLOW_RECURSIVE_TAGS = True


BACKEND_CLASS = PyslateJsonBackend

ALLOW_CACHE = False
CACHE_CLASS = None


PARSER_CLASS = PyParser

ALLOW_SPECIAL_TAGS = {
    "NUMBER": True,
}

DISABLE_NUMBER_FOR_VARIANT_TAGS = False

#
# lambdas used to decide about variant of tag which consits of a %{number} placeholder
#
NUMBERS = {
    "fb": lambda n: "" if n == 1 else "p",
    "en": lambda n: "" if n == 1 else "p",
    "pl": lambda n: "" if n == 1 else ("f" if n % 10 in [2, 3, 4] and n % 100 not in [12, 13, 14] else "p"),
}

ALLOW_GRAMMAR_VARIANTS = True
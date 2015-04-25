__author__ = 'Aleksander Chrabaszcz'
from .cache import SimpleMemoryCache

from .backend import PyslateJsonBackend
from .parser import PyParser

# DO NOT ALTER THIS FILE!!!
# DO NOT ALTER THIS FILE!!!
# DO NOT ALTER THIS FILE!!!


class DefaultConfig(object):
    """
    DO NOT ALTER THIS CLASS!!!

    This config file contains default configuration and is part of the library, so changing anything there
    may make it hard to upgrade.

    If you want to overwrite defaults, please create an own function which instantiates DefaultConfig,
    overwrites some values and then gives it to Pyslate's constructor as keyword-argument "config".
    Please note you can use keyword-arguments to specify own parser, cache and backend
    in case it cannot be instantiated using the default constructor. Keyword arguments set in Pyslate constructor
    overwrite values from the config.
    """

    def __init__(self):
        """
        Constructor
        """

        self.GLOBAL_FALLBACK_LANGUAGE = "en"
        """
        If there is no tag value for a specified target language, then a fallback language is used.
        If there's no tag value in both a target and fallback language, then a global fallback is used.
        So, for example, if global fallback is "en" and fallback for "pl" is "pt", and we try to see tag value in "pl",
        but neither "pl" nor "pt" has required tag value, then we look the tag value in language "en".
        It's a very good idea to treat global fallback as the most important language
        and this tag value should ALWAYS be available.
        """

        self.FALLBACKS = {
        }
        """
        FALLBACKS - dict of language fallbacks where key is target language and value is the fallback language e.g.
        {
            "pl": "pt",
            "pt": "es",
        }
        In case of no "pl" fallback "pt" will be used, but fallbacks are not recursive.
        So if there's no tag value for "pl" and "pt", then it **DOESN'T** fall back to "es"
        but it just tries to use a global fallback language.
        """


        self.ALLOW_INNER_TAGS = True
        """
        Inner tags are fields specified in the tag value using "${}" syntax, e.g.
        "root_tag": "I want ${item_cookie#p}!"
        "item_cookie#p": "cookies"
        translation: "root_tag" => "I want cookies!"
        When set to false, inner tags are shown as plaintext, e.g.
        translation: "root_tag" => "I want ${item_cookie#p}!"
        """

        self.ALLOW_CACHE = False
        """
        Specifies if instance of Pyslate should cache any data..

        When ALLOW_CACHE is True, then the cache needs to be specified as a keyword argument in Pyslate constructor.
        You can see the API of the cache.SimpleMemoryCache to create your own implementation.
        
        **IMPORTANT:** If you supply a cache this way, then the class must have a default (parameter-less) constructor.
        """

        self.PARSER_CLASS = PyParser
        """
        Contains class used as a parser of tag value to get AST with plaintext and variable, inner tag and switch fields
        It's used if you don't specify own parser instance in Pyslate constructor's keyword-argument.
        Default implementation is done using PLY.
        """

        self.DISABLE_NUMBER_FOR_TAG_KEYS_WITH_VARIANT = False
        """
        If true, then it will prevent executing special number code (selecting correct variant
            for specified %{number} placeholder) if a specified tag key already contains a variant.
        """

        self.LOCALE_FORMAT_NUMBERS = True
        """
        If true, then all the floats being interpolated into variable fields are automatically localized
        using language-specific Pyslate.localize()
        """

        self.ALLOW_SWITCH_FIELDS = True
        """
        If enabled, then special switch field syntax will be enabled, e.g.
        "%{opt1?ans1|opt2?and2}" - this one will print "ans1" when the value of a "variant" argument is "opt1" and
        will print "ans2" when value is "opt2". If "variant" is none of these, then first-left answer is used.
        If disabled, then all switch fields in tag values WILL BE CONVERTED INTO EMPTY STRINGS!
        """

        self.GLOBAL_DECORATORS = {
            "capitalize": str.capitalize,
            "upper": str.upper,
            "lower": str.lower,
        }
        """
        Dict containing decorators which are available for all languages.
        Decorators can be appended at the end of the inner tag or variable field to convert the value in a specific way.
        E.g. considering there exists a tag with key-value "cookies": "I like cookies"
        >>> pyslate.t("cookies@upper")
        I LIKE COOKIES
        """

        self.LANGUAGE_SPECIFIC_DECORATORS = {
            "en": {
                "article": lambda name: ("an " if name[0].lower() in "aeiou" else "a ") + name,
            }
        }
        """
        Dict containing decorators available only for a specific language.
        They are also available if language is current language's fallback or a global language fallback.
        For information what decorators are - see doc of GLOBAL_DECORATORS variable.
        """

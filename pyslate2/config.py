__author__ = 'Aleksander Chrabaszcz'
from pyslate2.cache import SimpleMemoryCache

from pyslate2.backend import PyslateJsonBackend
from pyslate2.parser import PyParser

# DO NOT ALTER THIS FILE!!!
# DO NOT ALTER THIS FILE!!!
# DO NOT ALTER THIS FILE!!!


class DefaultConfig:
    """
    DO NOT ALTER THIS FILE!!!

    This config file contains default configuration and is part of the library, so changing anything there
    may make it hard to upgrade.

    If you want to overwrite defaults, please create an own function which instantiates DefaultConfig,
    overwrites some values and then give it to Pyslate's constructor as keyword-argument "config".
    Please note you can use keyword-arguments to specify own parser, cache and backend
    in case it cannot be instantiated using the default constructor.
    """

    def __init__(self):
        """
        Constructor
        """

        """
        If there is no tag value for a specified target language, then a fallback language is used.
        If there's no tag value in both a target and fallback language, then a global fallback is used.
        So, for example, if global fallback is "en" and fallback for "pl" is "pt", and we try to see tag value in "pl",
        but neither "pl" nor "pt" has required tag value, then we look the tag value in language "en".
        It's a very good idea to treat global fallback as the most important language
        and this tag value should ALWAYS be available.
        """
        self.GLOBAL_FALLBACK_LANGUAGE = "en"

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
        self.FALLBACKS = {
        }

        """
        Inner tags are fields specified in the tag value using "${}" syntax, e.g.
        "root_tag": "I want ${item_cookie#p}!"
        "item_cookie#p": "cookies"
        translation: "root_tag" => "I want cookies!"
        When set to false, inner tags are shown as plaintext, e.g.
        translation: "root_tag" => "I want ${item_cookie#p}!"
        """
        self.ALLOW_INNER_TAGS = True

        """
        Reference for a backend class which supplies tag values.
        If backend is not specified in Pyslate constructor's keyword-argument,
        then it's instantiated using a default constructor.
        IMPORTANT! This class must have a default (parameter-less) constructor.
        """
        self.BACKEND_CLASS = PyslateJsonBackend

        """
        Specifies if instance of Pyslate should cache any data.
        If true then self.CACHE_CLASS should reference a class being its implementation.
        """
        self.ALLOW_CACHE = False

        """
        When ALLOW_CACHE is True, then this field contains cache class used by Pyslate.
        You can see the API of the default implementation to create your own.
        IMPORTANT! This class must have a default (parameter-less) constructor.
        """
        self.CACHE_CLASS = SimpleMemoryCache

        """
        Contains class used as a parser of tag value to get AST with plaintext and variable, inner tag and switch fields
        Default implementation is done using PLY.
        """
        self.PARSER_CLASS = PyParser

        """
        If true, then it will prevent executing special number code (selecting correct variant
            for specified %{number} placeholder) if specified tag name already contains a variant.
        """
        self.DISABLE_NUMBER_FOR_TAG_KEYS_WITH_VARIANT = False

        """
        If true, then all the floats being interpolated into variable fields are automatically localized
        using language-specific Pyslate.localize()
        """
        self.LOCALE_FORMAT_NUMBERS = True

        """
        If enabled, then special switch field: "%{opt1?ans1|opt2?and2}" will be enabled, e.g.
        this one will print "ans1" when the value of a "variant" argument is "opt1" and
        will print "ans2" when value is "opt2". If "variant" is none of these, then first-left answer is used.
        If disabled, then all switch fields in tag values WILL BE CONVERTED into empty string!
        """
        self.ALLOW_SWITCH_FIELDS = True

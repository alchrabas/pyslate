__author__ = 'Aleksander Chrabaszcz'
from .cache import SimpleMemoryCache

from .backend import PyslateJsonBackend
from .parser import PyParser

 #####    ####           #    #   ####    #####
 #    #  #    #          ##   #  #    #     #
 #    #  #    #          # #  #  #    #     #
 #    #  #    #          #  # #  #    #     #
 #    #  #    #          #   ##  #    #     #
 #####    ####           #    #   ####      #


 #    #   ####   #####      #    ######   #   #
 ##  ##  #    #  #    #     #    #         # #
 # ## #  #    #  #    #     #    #####      #
 #    #  #    #  #    #     #    #          #
 #    #  #    #  #    #     #    #          #
 #    #   ####   #####      #    #          #

# NOTICE:
# This config file contains default configuration and is part of the library, so changing anything there
# may make it hard to upgrade. Override config values as specified in documentation string of DefaultConfig.

class DefaultConfig(object):
    """
    Default values for configuration options of Pyslate.

    If you want to overwrite defaults, create a function which instantiates DefaultConfig,
    overwrites some values and then gives it to Pyslate's constructor as keyword-argument "config".
    Please note you can use keyword-arguments to specify own parser, cache and backend
    in case it cannot be instantiated using the default constructor. Keyword arguments set in Pyslate constructor
    overwrite values from the config.
    """

    def __init__(self):
        """Initializer"""
        self.GLOBAL_FALLBACK_LANGUAGE = "en"
        """
        If there is no tag value for a specified target language, then a fallback language is used.
        If there's no tag value in both a target and fallback language, then a global fallback is used.
        So, for example, if global fallback is "en" and fallback for "pl" is "pt", and we try to see tag value in "pl",
        but neither "pl" nor "pt" has required tag value, then we look the tag value in language "en".
        It's a very good idea to treat global fallback as the most important language
        and this tag value should ALWAYS be available.

        Default: "en"
        """

        self.FALLBACKS = {
        }
        """
        Dictionary of language fallbacks where key is target language and value is the fallback language e.g::

            {
                "pl": "pt",
                "pt": "es",
            }

        In case of no "pl" fallback "pt" will be used, but fallbacks are not recursive.
        So if there's no tag value for "pl" and "pt", then it **DOESN'T** fall back to "es"
        but it just tries to use a global fallback language.

        Default: ``{}``
        """


        self.ALLOW_INNER_TAGS = True
        """
        Inner tags are fields specified in the tag value using ``${}`` syntax, e.g::

            "root_tag": "I want ${item_cookie#p}!"
            "item_cookie#p": "cookies"

        translation: ``"root_tag" => "I want cookies!"``
        When set to ``False``, inner tags are shown as plaintext, e.g.
        translation: ``"root_tag" => "I want ${item_cookie#p}!"``

        Default: ``True``
        """

        self.ALLOW_CACHE = True
        """
        Specifies if instance of Pyslate should cache any data.

        When ALLOW_CACHE is True, then the cache needs to be specified as a keyword argument in Pyslate constructor.
        You can see the API of the cache.SimpleMemoryCache to create your own implementation.
        
        .. NOTE::
           If you supply a cache this way, then the class must have a default (parameter-less) constructor.

        Default: ``True``
        """

        self.PARSER_CLASS = PyParser
        """
        Contains class used as a parser of tag value to get AST with plaintext and variable, inner tag and switch fields
        It's used if you don't specify own parser instance in Pyslate constructor's keyword-argument.
        Default implementation is done using PLY parser generator.

        Default: ``PyParser``
        """

        self.OVERWRITE_VARIANT_ON_NUMBER = False
        """
        Enables completely overwriting the variant iwth a special number code (selecting correct
        variant for specified ``%{number}`` placeholder) even if a specified tag key already contains a variant.
        If set to false, then number variant is prepended as the first letter of the variant.

        Default: ``False``
        """

        self.LOCALE_FORMAT_NUMBERS = True
        """
        If true, then all the floats being interpolated into variable fields are automatically localized
        using language-specific :obj:`Pyslate.localize <pyslate.pyslate.Pyslate.localize>`

        Default: ``True``
        """

        self.ALLOW_SWITCH_FIELDS = True
        """
        If enabled, then special switch field syntax will be enabled, e.g.
        ``%{opt1?ans1|opt2?and2}`` - this one will print "ans1" when the value of a "variant" argument is "opt1" and
        will print "ans2" when value is "opt2". If "variant" is none of these, then first-left answer is used.
        If disabled, then all switch fields in tag values will be **silently** converted into empty strings.

        Default: ``True``
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

        Default: see :ref:`Available_Decorators`
        """

        self.LANGUAGE_SPECIFIC_DECORATORS = {
            "en": {
                "article": lambda name: ("an " if name[0].lower() in "aeiou" else "a ") + name,
            }
        }
        """
        Dict containing decorators available only for a specific language.
        They are also available if language is current language's fallback or a global language fallback.
        For information what decorators are - see doc of :attr:`GLOBAL_DECORATORS <pyslate.config.DefaultConfig.GLOBAL_DECORATORS>` variable.

        Default: see :ref:`Available_Decorators`
        """

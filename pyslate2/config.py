__author__ = 'Aleksander Chrabaszcz'
from pyslate2.cache import PyslateCache



from pyslate2.backend import PyslateJsonBackend
from pyslate2.parser import PyParser

# DO NOT CHANGE THIS FILE!!!


class PyslateConfig:
    """
    DO NOT CHANGE THIS FILE!!!

    This config file contains default configuration and is part of the library, so changing anything here
    may make it hard to update correctly.

    If you want to overwrite defaults, please create an own function which
        instantiates PyslateConfig and overwrites interesting values and then give it to
        Pyslate's constructor in keyword-argument "config". Please note you can use keyword-arguments to specify own
        parser, cache and backend in case it cannot be just a new instance of class with a default constructor.
    """

    def __init__(self):

        """
        If there is no tag for a specified target language, then a fallback language is used.
            So, for example, if fallback for "pl" is "en" and then we look for tag "help_me" in language "pl"
            and there is no such tag, then it'll take contents of the "help_me" for "en" language.

        GLOBAL_FALLBACK_LANGUAGE - fallback used when there is no tag in target language
            and its fallback language (if defined)
        """
        self.GLOBAL_FALLBACK_LANGUAGE = "en"

        """
        FALLBACKS - dict of language fallbacks where key is target language and value is the fallback language e.g.
        {
            "pl": "en",
        }
        means that in case of no "pl" tag "en" will be used. Fallbacks are not recursive. e.g.
        {
            "pl": "pt",
            "pt": "es",
        }
        In case of no "pl" fallback "pt" will be used, but if there's no tag for "pt", then it DOESN'T fall back to "es"
            but it just tries to use global fallback language.
        """
        self.FALLBACKS = {
        }

        """
        Inner tags are tags defined in the translated tag's contents using "${}" syntax, e.g.
        "root_tag": "I want ${item_cookie#p}!"
        "item_cookie#p": "cookies"
        translating "root_tag" gives "I want cookies!"
        When disabled, they are shown as uninterpreted plaintext, e.g. then
        translating "root_tag" gives "I want ${item_cookie#p}!"
        """
        self.ALLOW_INNER_TAGS = True

        """
        Reference for backend class used to get translation tags contents.
        """
        self.BACKEND_CLASS = PyslateJsonBackend

        """
        Specifies if instance of Pyslate should cache any data.
        """
        self.ALLOW_CACHE = False

        """
        When ALLOW_CACHE is true, then this field contains class for cache used by Pyslate.
        You can see the API in the class being default implementation.
        """
        self.CACHE_CLASS = PyslateCache

        """
        Contains class used as a parser for tag contents to get AST with plaintext and special structures.
        It's obliged to have method "parse".
        Default implementation is done in PLY.
        """
        self.PARSER_CLASS = PyParser

        """
        List of uppercased placeholder names which execute some special code when found in the tag contents.
            If disabled then they are treated as a normal placeholder,
            so its value should be specified in keyword arguments of Pyslate.translate method
        """
        self.ALLOW_SPECIAL_PLACEHOLDERS = {
            "NUMBER": True,
        }

        """
        If true, then it will prevent executing number-specific code (selecting correct variant
            for specified %{number} placeholder) if specified tag name already contains a variant.
        """
        self.DISABLE_NUMBER_FOR_VARIANT_TAGS = False

        """
        Fallback language used instead of GLOBAL_FALLBACK_LANGUAGE when target language and its fallback don't have
            NUMBER function (which decides about correct tag variant) specified in locale.py
        """
        self.NUMBER_FALLBACK_LANGUAGE = "en"

        """
        If true, then numbers specified for special number tag are localized using language-specific Pyslate.localize()
        """
        self.LOCALE_FORMAT_NUMBERS = True

        """
        If enabled, then special variants structure: "%{opt1?ans1|opt2?and2}" will be enabled, e.g.
        this one will print "ans1" when value of a special keyword-argument "variant" is "opt1" and
        will print "ans2" when value is "opt2". If variant is none of these, then first-left answer "ans1" will be used.
        If disabled, then all variant structures in tag contents WILL BE REPLACED BY AN EMPTY STRING!
        """
        self.ALLOW_VARIANTS_STRUCTURE = True

.. _advanced_examples:

Advanced examples
=================
This page contains advanced examples formatted similarly to the basic examples available in the README:
code, tags in multiple languages and result.
So it's not to present concrete functions of the library, but show general examples what things can be done using Pyslate.

Advanced switch fields
----------------------

::

    "talking_the_same": {
        "en": "I told %{sb:m?him|f?her} it's stupid and %{sb:m?|f?s}he told me the same.",
        "pl": "Powiedział%{me:m?em|f?am} %{sb:m?mu|f?jej}, że to głupie, a on%{sb:m?|f?a} powiedział%{sb:m?|f?a} mi to samo.",
    }

    >>> pyslate_en.t("talking_the_same", me="f", sb="f")
    I told her it's stupid and she told me the same.
    >>> pyslate_en.t("talking_the_same", me="m", sb="m"))

    >>> pyslate_pl.t("talking_the_same", me="f", sb="f")
    "Powiedziałam jej, że to głupie, a ona powiedziała mi to samo."
    >>> pyslate_pl.t("talking_the_same", me="m", sb="m"))
    "Powiedziałem mu, że to głupie, a on powiedział mi to samo."

Example 2 - Complicated number format
-------------------------------------
First thing: We have both singular and plural forms in the single translation tag, even though it's less readable.
It's possible thanks to "tag_v" special variable, which always contains original tag variant, even if for example
"item_mug#y" had to be fallbacked to "item_mug" because there was no specific variant tag.
Even more, it's possible to mix these two ways of representing variants, especially useful if target language is more complicated than the original one.

# TODO!!!
::

    "giving_thing": {
        "en": "I give you ${item_%{name}}",
        "pl": "Daję ci ${item_%{name}#a}", # TODO!!! # TODO!!! # TODO!!!
    },
    "item_mug": {
        "en": "${number} mug%{tag_v:x?|y?s}",
        "pl": "${number} kub%{tag_v:x?ek|w?ki|y?ków}",
    },
    "item_cup": {
        "en": "${number} mug%{tag_v:x?|y?s}",
        "pl": "filiżank%{tag_v:x?a|a?ę}",
    }
    "item_cup#w": {
        "pl": "${number} filiżanki",
    },
    "item_cup#y": {
        "pl": "${number} filiżanek",
    }

As you can see, for Polish you have to use a different case (accusative), but only for a singular form of a word "cup".
It's not necessary for a mug, though (no easy way to learn that, you just need to know that ;]).
Another magic (which was already used somewhere else too) is having option "x?" in a switch field.
"x" variant is required to be never used, so it cannot ever be matched in a standard way. But it's first left case, so it can be matched as default option
in case nothing else can be matched. That's the case when you request the most basic form of a word (singular).

Example 3 - Advanced tag variants
---------------------------------
Somewhere in the readme I've said that switch field matches the value which is equal to a specified variant.

::

    "aaa": {
        "en": "I have helped those camels.",
        "pl": "Pomogłem tamtym wielbłądom.",
    }


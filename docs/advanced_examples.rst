.. _advanced_examples:

Advanced examples
=================
This page contains advanced examples formatted similarly to the basic examples available in the README:
code, tags in multiple languages and result.
So it's not to present concrete functions of the library, but show general examples what things can be done using Pyslate.

Example 1 - Advanced switch fields
----------------------------------
It's possible to use multiple variables to control switch fields.

::

    "talking_the_same": {
        "en": "I told %{sb:m?him|f?her} it's stupid and %{sb:m?|f?s}he told me the same.",
        "pl": "Powiedział%{me:m?em|f?am} %{sb:m?mu|f?jej}, że to głupie, a on%{sb:m?|f?a} powiedział%{sb:m?|f?a} mi to samo.",
    }

    >>> pyslate_en.t("talking_the_same", me="f", sb="f")
    I told her it's stupid and she told me the same.
    >>> pyslate_en.t("talking_the_same", me="m", sb="m"))
    I told him it's stupid and he told me the same.

    >>> pyslate_pl.t("talking_the_same", me="f", sb="f")
    "Powiedziałam jej, że to głupie, a ona powiedziała mi to samo."
    >>> pyslate_pl.t("talking_the_same", me="m", sb="m"))
    "Powiedziałem mu, że to głupie, a on powiedział mi to samo."


Example 2 - Advanced tag variants
---------------------------------
| Somewhere in the README I've said that switch field matches the value which is equal to a specified variant.
| It's not entirely true. It matches an option which is **contained in** switch variable's value.
| It means letters representing specific variants can be joined into one string e.g. "pma" to have accusative masculine for plural.
| It's advised to use exactly this order: NUMBER, GENDER, CASE. It is required to have NUMBER left-most letter if it exists.

::

    "show_the_way": {
        "en": "I have shown the way to the ${%{benefactor}}.",
        "pl": "Wskazałem drogę ${%{benefactor}#d} ."
    },
    "traveler": {
        "en": "traveler",
        "pl": "podróżnik"
    },
    "traveler#p": {
        "en": "travelers",
        "pl": "podróżnicy"
    },
    "traveler#pd": {
        "pl": "podróżnikom"
    },
    "driver": {
        "en": "driver",
        "pl": "kierowca"
    },
    "driver#p": {
        "en": "drivers",
        "pl": "kierowcy"
    },
    "cyclist": {
        "en": "cyclist",
        "pl": "cyklista"
    },
    "cyclist#d": {
        "pl": "cykliście"
    },

    # first example - correct
    >>> pyslate_en.t("show_the_way", number=5, benefactor="traveler")
    I have shown the way to the travelers.
    >>> pyslate_pl.t("show_the_way", number=5, benefactor="traveler")
    Wskazałem drogę podróżnikom.

    # second example - fallback to shorter variant: driver#pd -> driver#p
    >>> pyslate_en.t("show_the_way", number=5, benefactor="driver")
    I have shown the way to the drivers.
    >>> pyslate_pl.t("show_the_way", number=5, benefactor="driver")
    Wskazałem drogę kierowcy.

    # third example - fallback to base form: cyclist#pd -> cyclist#p -> cyclist
    >>> pyslate_en.t("show_the_way", number=5, benefactor="cyclist")
    I have shown the way to the cyclist.
    >>> pyslate_pl.t("show_the_way", number=5, benefactor="cyclist")
    Wskazałem drogę cyklista.


| In the first code example, it correctly guesses the number and case for both English and Polish.
| In the second example it's ok in English, but there's no *driver#pd* variant for Polish, so it removes the right-most letter from variant and tries again. It finds the *driver#p* tag so it's used as a fallback.
| In the third example, Polish and English have no plural form, so it's not used. In Polish *cyclist#d* variant is defined, but the fallback mechanism tries: *cyclist#pd*, then *cyclist#p* and *cyclist*. So both English and Polish fallback to base form.


Example 3 - Complicated number format
-------------------------------------
| First thing: We have both singular and plural forms in the single translation tag, even though it's less readable.
| It's possible thanks to "tag_v" special variable, which always contains original tag variant, even if for example
| "item_mug#y" had to be fallbacked to "item_mug" because there was no specific variant tag.
| Even more, it's possible to mix these two ways of representing variants, especially useful if target language is more complicated than the original one.

::

    "giving_thing": {
        "en": "I give you ${item_%{name}}",
        "pl": "Daję ci ${item_%{name}#a}",
    },
    "item_mug": {
        "en": "${number} mug%{tag_v:s?|p?s}",
        "pl": "${number} kub%{tag_v:s?ek|w?ki|p?ków}",
    },
    "item_cup": {
        "en": "${number} cup%{tag_v:s?|p?s}",
        "pl": "filiżank%{tag_v:x?a|a?ę}",
    }
    "item_cup#w": {
        "pl": "${number} filiżanki",
    },
    "item_cup#p": {
        "pl": "${number} filiżanek",
    }

    >>> pyslate_en.t("giving_thing", number=1, name="cup")
    I give you 1 cup.
    >>> pyslate_en.t("giving_thing", number=5, name="cup")
    I give you 5 cups.
    >>> pyslate_pl.t("giving_thing", number=1, name="cup")
    Daję ci filiżankę.
    >>> pyslate_pl.t("giving_thing", number=5, name="cup")
    Daję ci 5 filiżanek.

| As you can see, for Polish you have to use a different case (accusative), but only for a singular form of a word "filiżanka" ("cup").
| It's not necessary for a word "kubek" ("mug"), though.
| tag value "filiżank%{tag_v:x?a|a?ę}" contains
| Another trick (which was already used somewhere else too) is having option "x?" in a switch field.
| "x" variant is required to be never used, so it can never be matched with value of variable. But it's first left, so it is matched as default option when nothing else can be matched.
| That's the case when you request the most basic form of a word (singular nominative form).

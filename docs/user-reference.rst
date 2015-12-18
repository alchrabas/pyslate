Pyslate syntax reference
========================

Decorators
----------
Decorators are constructs applicable to tags or variable fields to modify their value.
They are python functions which take tag value string as input and return output string.
They are added after the end of tag key and are prefixed by “@”.
They are left-associative e.g. “**some_tag@article@capitalize**” means first adding an article, then capitalizing the first letter.

::

    {
        "buying_toy": {
            "en":  "I've bought ${toy_%{name}@article}."
        },
        "toy_rocking_horse": {
            "en": "rocking horse"
        },
        "toy_autosan": {
            "en": "autosan"
        }
    }

    >>> pyslate_en.t("buying_toy", name="rocking_horse")
    I've bought a rocking horse.
    >>> pyslate_en.t("buying_toy", name="autosan")
    I've bought an autosan.


Apart from built-in decorators it’s possible to define custom ones.

::

    {
        "some_message": {
            "en":  "Important message"
        },
        message_container": {
            "en":  "Message is: ${some_message@add_dots}"
        }
    }

    def add_dots(value):
        return ".".join(value)

    pyslate_en.register_decorator("add_dots", add_dots)

    >>> pyslate_en.t("message_container")
    Message is: I.m.p.o.r.t.a.n.t. .m.e.s.s.a.g.e

    >>> pyslate_en.t("message_container@add_dots")
    M.e.s.s.a.g.e. .i.s.:. .I...m...p...o...r...t...a...n...t... ...m...e...s...s...a...g...e


It's possible to decorate both requested tag, inner tag fields and variable fields.
In the last command, value of "some_message" tag gets dots added and then the whole texts gets dots added.
There are three dots between the letters, because second decorator adds dots between
every single character, including dots added by first decorator.

.. _Available_Decorators:

Available decorators
^^^^^^^^^^^^^^^^^^^^

By default Pyslate provides the following decorators in the default scope:

 - ``capitalize`` - make the first character have upper case and the rest lower case
 - ``upper`` - convert to uppercase
 - ``lower`` - convert to lowercase

For English an additional decorator is available:

 - ``article`` - add *a* or *an* article to a word. *An* is added if the first letter of the word is a vowel, *a* otherwise.


Custom functions
----------------
Custom functions allow you to do everything.
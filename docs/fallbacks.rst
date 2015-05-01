.. _fallbacks:

Fallbacks in Pyslate
====================
On the README page I've said that one of Pyslate's advantages is a powerful fallback mechanism.
In general, it means that if something is not available in the expected form/language, then Pyslate wisely selects the most suitable form from the available using very simple rules.

Tag variant fallback
--------------------
Every tag key constraints of base and variant: e.g. **sweet_cookie**#*p*. A tag without any variant is called a base tag.
If it is so, then in case expected tag doesn't exist, then its base tag is used instead.
sweet_cookie#p -> sweet_cookie
That's why it's necessary to guarantee that if there's a variant tag, then its base tag should ALWAYS be available.
But it's more sophisticated than that. If you have a tag with variant consisting of many variant letters, specifying number, gender and case, then
fallbacking happens from most exact to the least exact variant tag, and in case it's unsuccessful then base tag is used.
::

    sweet_cookie#png -> sweet_cookie#pn -> sweet_cookie#p -> sweet_cookie

Language fallback
-----------------
Pyslate supports incremental translations, so the system can be used before all the translations are completed.
In such case, when there's no base tag in the target language, then its fallback language (specified in the config) is used instead.
There's also a global fallback language - the original language where tags are guaranteed to always exist.
For example when "es" is the fallback language for "pt", then Spanish translation is used when there's no Portuguese.
In such situation the tag variant fallback happens for every language in order.
::

    (pt)sweet_cookie#png -> (pt)sweet_cookie#pn -> (pt)sweet_cookie#p -> (pt)sweet_cookie -> (es)sweet_cookie#png -> (es)sweet_cookie#pn -> (es)sweet_cookie#p -> (es)sweet_cookie

If there's no tag for target language or its fallback language, then its global fallback is used (usually it's English).
It also uses full tag variant fallback mechanism.

Decorator and function fallback
-------------------------------
It uses language fallback. There are no function/decorator variants, so it's just looking for fallback language and then global fallback.
Just keep in mind that some decorators can be language-specific, so they might have no fallback.


Locale fallback
---------------
Then locale is no available e.g. "en-GB", then more generic "en" is used. So it's better to specify locale as well as possible.

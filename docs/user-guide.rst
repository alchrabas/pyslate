.. _user-guide:

User guide
==========
Managing translations from the perspective of the translator.

Introduction
------------

In this article you'll learn how to translate (internationalize&localize) the messages as a translator - when you have no idea about its programmatic context.

All these examples will be posted in the same form: a box with all tags in English, a box with all tags in Pirate English.
Then there will be some examples of using these tags in the real-life context.

.. Note::
    Such examples are something you usually don't have access to as a translator.

First I'll explain what tag is. Tag is a pair of text strings: a key and a value.

 - **Value** is the text visible for users of the program - the part you have to translate.
 - **Key** is text's identifier invisible for users - you should keep it the same, because translating is basically supplying a different tag value for the same key.

All examples will use the simple syntax: ``TAG_KEY => TAG_VALUE``

Hello message
-------------
As I cannot assume you know any language besides English, we'll start with translating English to Pirate English.

**English**
::

    hello => Hello guys

It's easy. You read the value of the "hello" tag and provide a translation.

**Pirate English**
::

   hello => Ahoy comrades!

This tag value is exactly what users will see, so there's no need to show any examples.

Interpolated variables
----------------------

Sometimes it's necessary to mention in the message something specified from outside.
Just think about a message dialog 'Do you want to remove a file "mypicture.png"?'
This file name is not always the same so there must be a way for programmer to specify it and there needs to be a way for a translator to show it in the dialog.
That's why there exists a special structure, called a **variable field**. It's denoted as **%{variable_name}** which is
replaced by Pyslate during program execution. The "variable_name" is identifier of value which should be interpolated here.
The only easy way to learn what can stand for "variable_name" is to thoroughly read the original translation.

**English**
::

    file_removal => Do you want to remove a file "%{file_name}"?

So now we know that name of the file is specified using the identifier "file_name". So all we need to do is translate it in the same manner.

**Pirate English**
::

    file_removal => Do ye want to scuttle a file "%{file_name}"?

Example is easy to guess, so let's go on.

.. admonition:: English Example
    :class: Note

    | Do you want to remove a file "ship.png"?

.. admonition:: Pirate English Example
    :class: Note

    | Do ye want to scuttle a file "ship.png"?

Interpolated variables - numbers
--------------------------------

The values interpolated into the variable fields can be also the numbers.

**English**
::

    rum_barrel   => I posess a barrel of the finest rum.
    rum_barrel#p => I posess %{number} barrels of the finest rum.

What's that? When the programmer calls a variable identifier "number" then some magic happens. As you see there are two forms of the same tag.
"rum_barrel" is called a base tag, while "#p" is called a tag variant (because it's a variant of a base tag).
Then, depending on the value of the **%{number}**, a different version of a tag can be selected.
In English it's "rum_barrel" (singular) when **%{number}** is 1, and "rum_barrel#p" (**p**\ lural) when **number** is not 1.
There are just two forms, but some languages have much more. Let's assume our Pirate English has a different form
of noun when **%{number}** is 2, and then "-es" is appended instead of "-s" to the end of the noun.
We assume the programmer already took care of specifying pluralization rules for our language, so all we have to do is learning what letter is used when the **%{number}** is 2.
After a short look into cheatsheet (TODO LINK) we learn that in such situation we should add "#t" variant (**t**\ wo). Okay, here we go.

**English**
::

    rum_barrel   => I'ave a barrel o' best rum.
    rum_barrel#t => I'ave %{number} barreles o' best rum.
    rum_barrel#p => I'ave %{number} barrels o' best rum.

Now some examples:

.. admonition:: English Example
    :class: Note

    | I posess a barrel of the finest rum.
    | I posess 2 barrels of the finest rum.
    | I posess 5 barrels of the finest rum.
    | I posess 17 barrels of the finest rum.

.. admonition:: Pirate English Example
    :class: Note

    | I'ave a barrel o' best rum.
    | I'ave 2 barreles o' best rum.
    | I'ave 5 barrels o' best rum.
    | I'ave 17 barrels o' best rum.

Curious what language has a different pluralization when there are exactly two items? It's the case for Arabic and many others.
We are prepared for that.

Fallbacks in Pyslate
--------------------
Pyslate has a powerful fallback mechanism. It means if something is not available in the expected form/language,
then Pyslate is selecting the best alternative.

**Tag variant fallback**

Every tag key constraints of base and variant: e.g. *sweet_cookie*\ #\ **p**.
In case expected tag doesn't exist, then its base tag is used.
sweet_cookie#p -> sweet_cookie
It should always be guaranteed that a base tag exists if any variant exists.
If you have a tag with variant consisting of many variant letters then matching is done from the most to least exact:
::

    . sweet_cookie#png -> sweet_cookie#pn -> sweet_cookie#p -> sweet_cookie

**Language fallback**

Pyslate supports incremental translations, so the system can be used before all the translations are completed.
If there's no matching tag in the target language, then the whole procedure is run again for the fallback language.
E.g. when fallback language for Portuguese is Spanish:
::

    (pt)sweet_cookie#p -> (pt)sweet_cookie -> (es)sweet_cookie#p -> (es)sweet_cookie

If there's no tag for target language or its fallback language, then its global fallback is used (usually it means English).

Switch fields - different forms of the same text
------------------------------------------------

Now it's time for another special structure called a **switch field**.
It's denoted '%{identifier:option1?answer1|option2?answer2}' which means "if value for 'identifier' is equal to 'option1' then show 'answer1',
if 'identifier' is equal to 'option2' then use 'answer2'. If none of these, then use the first answer from the left - 'answer1' in this case".
'identifier' is name of some variable, very similar to 'variable_name' or 'number' from the previous examples.

**English**
::

    sabre_statement => I have a sabre, %{state:sharp?a finely sharped one|blunt?which is going to be sharpened soon}.

Okay, so we shouldn't translate the identifier or its options ("state", "sharp", "blunt"), as we have no control over these.
But we can translate answers, which are visible for users.

**Pirate English**
::

    sabre_statement => Arr! I'ave a saber, %{state:sharp?a well sharp'd one|blunt?which be goin' to be sharp'd before I sail out}.

.. admonition:: English Example
    :class: Note

    | I have a sabre, a finely sharped one.
    | I have a sabre, which is going to be sharpened soon.

.. admonition:: Pirate English Example
    :class: Note

    | Arr! I'ave a saber, a well sharp'd one.
    | Arr! I'ave a saber, which be goin' to be sharp'd before I sail out.

Inner tag fields
----------------

Now it's time for the last special structure available - an **inner tag field**.
In short, it allows you to show any other tag on any position in the text.
It's denoted **${tag_name}**, where tag_name is any of existing tag keys.

**English**
::

    eat_breakfast   => I was eating breakfast. ${was_good}.
    eat_supper:     => I was eating supper. ${was_good}.
    was_good:       => It was really good.

It's quite easy. We translate, but don't touch stuff inside of ${}. It's a quite simple example menat to just have a bit less to copy&paste (even though we are pirates),
but there happen complicated situations where using this structure is unavoidable.

**Pirate English**
::

    eat_breakfast   => I was eatin' breakfast. ${was_good}.
    eat_supper      => I was eatin' supper. ${was_good}.
    was_good:       => 'twas really jolly.

.. admonition:: English Example
    :class: Note

    | I was eating breakfast. It was really good.
    | I was eating supper. It was really good.

.. admonition:: Pirate English Example
    :class: Note

    | I was eatin' breakfast. 'twas really jolly.
    | I was eatin' supper. 'twas really jolly.

Variable tag field in inner tag field
-------------------------------------

We need to go deeper.

**English**
::

    look_at:        => Hey! Look at ${state_%{item}}.
    state_sabre:    => a sharp sabre
    state_gun:      => a shiny pistol

Oh, look, a **variable field** inside of **inner tag field**. It means **variable field** is evaluated first,
which produces *some* text (e.g. "ABC"), which is merged with "state_", which created a name of the inner tag
(e.g. "state_ABC"), which is then looked for on the list of tag keys. Quite complicated, but is it a problem for a translator like you?
**%{item}** can potentially hold any value you can think, but it's possible to guess that the only possible values are de facto "sabre" and "gun",
because we see that inner tag must start with "state_". We can  assume it always produce the valid (existing) tags.
There cannot be any other in our Pirate language if there aren't such in original language.

**Pirate English**
::

    look_at:        => Ahoy! Look at ${state_%{item}}.
    state_sabre:    => a sharp saber
    state_gun:      => a nice firearm

.. admonition:: English Example
    :class: Note

    | Hey! Look at a sharp sabre.
    | Hey! Look at a shiny pistol.

.. admonition:: Pirate English Example
    :class: Note

    | Ahoy! Look at a sharp saber.
    | Ahoy! Look at a nice firearm.

Another success, so now something what our Pirate English will not cope with.

Switch field and inner tag field cooperation
--------------------------------------------

The already presented features are enough for our Pirate English example, but unfortunately Pirate English
looks quite similar to English. All the difference is changing a few words, but there are real languages which are much different.
I'm speaking about fusional languages. If you are not working with them, then you don't have to read further, but you may still find it interesting.
The following example will be much more complicated, but I hope it'll be explained precisely.
In Polish (and Russian, German... and many others) every noun has a grammatical form (gender).
Let's see: "szabla" (a sabre) is feminine (f), while "pistolet" (a pistol) is masculine (m).
This grammatical form is very important to set the correct suffix for adjectives describing the noun.
Let's see an example:

| This is a new pistol. => To jest now\ **y** pistolet.
| This is a new sabre. => To jest now\ **a** szabla.

| "To jest" (This is) part is the same for both items, but the suffix appended to the stem "now-" is based on the gender of the noun:
| "m" => "-y"
| "f" => "-a"
| "n" => "-e"

**English**
::

    presentation_text:  => This is a new ${item_%{item_name}}.
    item_sabre:         => sabre
    item_pistol:        => pistol

I hope this part is quite easy. Using the same deduction as in the previous example we know that item_name can be only "sabre" or "pistol".
Now we need to prepare a translation for Polish.
We start with translating the items. It's possible to specify the grammatical form for every tag, so we do it here:

**Polish**
::

    item_sabre: => szabla
             form: f
    item_pistol: pistolet
             form: m

| Okay, we have translated items, but there's the toughest part. At the first glance it should be something like:
| presentation_text: To jest now%{**SOMETHING**:m?y|f?a|n?e} ${item_%{item_name}}.

What to set into **SOMETHING**? How can we guess what item is it? Should we ask a programmer to create a special variable for us?
It's a very bad idea, because it would significantly complicate the translation process.
That's why there's a special way in which inner tag fields can cooperate with switch fields.

**Polish**
::

    presentation_text:  => To jest now%{obj_g:m?y|f?a|n?e} ${obj_g:item_%{item_name}}.

That's right. We have specified an identifier for an inner tag (*obj_g*), which is then used as an identifier of a variable which is used in a switch field.
The inner tag's identifier gets the grammatical form contained in an inner tag. It is then transported to the switch field which makes the correct decision.

So the full Polish translation looks like that:
**Polish**
::

    presentation_text:  => To jest now%{obj_g:m?y|f?a|n?e} ${obj_g:item_%{item_name}}.
    item_sabre:         => szabla
                     form: f
    item_pistol:        => pistolet
                     form: m


If you are translating to a fusional language then I hope you've learned how does it work. If you don't know any of such, then these examples can be hard to understand.

Appendix I - correct variant letters for numbers and cases
----------------------------------------------------------

As it was already mentioned, variants are specified by single-letter identifiers.
Every letter has some contractual meaning and specific letters are not imposed by Pyslate (with exception of pluralization letters, which are based on language locale).

Letters that are reserved to be used for pluralization forms:

    - "" (empty) - singular - base form
    - z - zero - when there are no elements
    - t - **T**\ wo - plural form for 2 or numbers treated like 2.
    - w - fe\ **W** - form used for *a few* elements (usually 3, 4) or treated like *a few*
    - p - plural (a.k.a. many) - form used for all the rest

They are unused for most of languages.

Suggestion what letters should be used for the following gender forms:

    - m - masculine
    - f - feminine
    - n - neuter

There's suggestion what letters should be used for the following (latin) cases in fusional languages:

    - "" (empty) - nominative - base form
    - g - genitive
    - d - dative
    - a - accusative
    - b - ablative
    - l - locative
    - v - vocative

It's worthless to try to supply all the forms, even if the language supports them. Use only those really needed in the translation system.
If language you are translating to supports more than that - you can use any of "unused" letters. It's just advised to avoid using "x".

If variant tag contains all these data, then letters in a variant are advised to be used in the following order: plural form, gender form, case.
For example: small_stone#pmg (plural, masculine, genitive). This order guarantees the fallback process most effective.

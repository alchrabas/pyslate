User guide
==========
Managing translations from the perspective of the translator.

Introduction
============
If you are a programmer who knows how to use Pyslate in code - forget everything about it. If you aren't - that's better.
Now you'll learn how to translate the messages when you have no idea about its programmatic context.

As I cannot assume you know any (and which) language besides English, my goal here will be to provide simple examples
where you have to translate English to Pirate English.

All examples will be posted in form: a box with all tags in English, a box with all tags in Pirate English.
Then there will be some examples of using these tags in the real-life context. That's something you often don't have access to as a translator.

Now you need an explanation what tag is. Tags is a pair of text strings: a key and a value.
Value is the text visible for users of the program - the part you have to translate.
The key is text's identifier invisible for users - you should keep it the same, because translating is basically
supplying a different tag value in the same location, which is specified by the tag key.
All examples will use a simple syntax:
TAG_KEY: TAG_VALUE

Hello message
=============
English
hello: Hello guys!

It's easy. You read the value of the "hello" tag and provide a translation.

Pirate English
hello: Ahoy comrades!

That's exactly what users will see, so there's no need to show any examples.

Interpolated variables
======================
Sometimes it's necessary to mention in the message something specified from outside.
Just think about a message dialog 'Do you want to remove a file "mypicture.png"?'
This file name is not always the same so there must be a way for programmer
to specify it and there needs to be a way for a translator to mention it in the code.
That's why there exists a special structure, called a variable field. It's denoted as %{variable_name} which is
then replaced by the translation system during program execution. The "variable_name" is identifier of value which should be interpolated there.
The only easy way to learn what should be in place of "variable_name" is to thoroughly read the original translation.

English
file_removal: Do you want to remove a file "${file_name}"?

So now we know that name of the file is specified using the identifier "file_name". So all we need to do is translate it in the same manner.

Pirate English:
file_removal: Do ye want to scuttle a file "${file_name}"?

Example is easy to guess, so let's go on.

Interpolated variables - numbers
================================

Of course, the values interpolated into the variable fields can be also the numbers.

English
rum_barrel: I posess a barrel of the finest rum.
rum_barrel#h: I posess %{number} barrels of the finest rum.

What's that? When the programmer calls a variable identifier "number" then some magic happens. As you see there are two forms of the same tag.
"rum_barrel" is called a tag base, while "#h" is called a tag variant (because it's a variant of a base tag).
Then, depending on a value of the %{number}, a different version of a tag can be selected.
In English it's "rum_barrel" (singular) when "number" is 1, and "rum_barrel#h" (mucH) when "number" is more than 1.
There are just two forms, but some languages have much more. Let's assume our Pirate English has a different form
of noun when "number" is 2, which appends "-es" instead of "-s" to the end of the noun.
We assume the programmer already took care of specifying pluralization rules for our language, so all we have to do is learning what letter is used when the "number" is 2.
After a short look onto cheatsheet (TODO LINK) we learn that in such situation the variant is "#t" (Two). Okay, here we go.

Pirate English:
rum_barrel: I'ave a barrel o' best rum.
rum_barrel#t: I'ave %{number} barreles o' best rum.
rum_barrel#h: I'ave %{number} barrels o' best rum.

Now some examples:
English:
I posess a barrel of the finest rum.
I posess 2 barrels of the finest rum.
I posess 5 barrels of the finest rum.
I posess 17 barrels of the finest rum.

Pirate English:
I'ave a barrel o' best rum.
I'ave 2 barreles o' best rum.
I'ave 5 barrels o' best rum.
I'ave 17 barrels o' best rum.

Curious what language has a different pluralization when there are exactly two items? It's the case for Arabic and Welsh, and maybe others.
And we are prepared for that.

Switch fields - different forms of the same text
================================================
Now it's time for another special structure, which is called a switch field.
It's denoted '%{identifier:option1?answer1|option2?answer2}' which means "if value for 'identifier' is equal to 'option1' then show 'answer1',
if 'identifier' is equal to 'option2' then use 'answer2'. If none of these, then use the first answer from the left - 'answer1' in this case.
'identifier' is name of some variable, very similar to 'variable_name' or 'number' from the previous examples.

English
sabre_statement: I have a sabre, %{state:sharp?a finely sharped one|blunt?which is going to be sharpened soon}.

Okay, so we shouldn't translate the identifier or its options ("state", "sharp", "blunt"), as we have no control over these.
But we can translate answers, which are visible for users.

Pirate English
sabre_statement: Arr! I'ave a saber, %{state:sharp?a well sharp'd one|blunt?which be goin' to be sharp'd before I sail out}.

Examples
English
I have a sabre, a finely sharped one.
I have a sabre, which is going to be sharpened soon.

Pirate English
Arr! I'ave a saber, a well sharp'd one.
Arr! I'ave a saber, which be goin' to be sharp'd before I sail out.

Inner tag fields
================
Now it's time for the last special structure available - a inner tag field.
In short, it allows you to mention and get value of another tag in any position in the text you like.
It's denoted ${tag_name}, where tag_name is any of available tag keys.

English
eat_breakfast: I was eating breakfast. ${was_good}.
eat_supper: I was eating supper. ${was_good}.
was_good: It was really good.

It's quite easy. We translate, but don't touch stuff inside of ${}. It's a quite simple example just to have a bit less to copy&paste (even though we are pirates),
but there are complicated situations where using that is unavoidable.

Pirate English
eat_breakfast: I was eatin' breakfast. ${was_good}.
eat_supper: I was eatin' supper. ${was_good}.
was_good: 'twas really jolly.

Examples
English
I was eating breakfast. It was really good.
I was eating supper. It was really good.

Pirate English
I was eatin' breakfast. 'twas really jolly.
I was eatin' supper. 'twas really jolly.

Variable tag field in inner tag field
=====================================
We need to go deeper.

English
look_at: Hey! Look at ${state_%{item}}.
state_sabre: a sharp sabre
state_gun: a shiny pistol

Oh, look, a variable field inside of inner tag field. It means variable field is evaluated first,
which produces *some* text (e.g. "ABC"), which is merged with "state_", which produces name of the inner tag
(e.g. "state_ABC"), which is then looked for on the list of tag keys. Quite confusing, but is it a problem for a translator like you?
%{item} can potentially hold any value you can think, but it's possible to guess that the only possible values are de facto "sabre" and "gun",
because we see that inner tag must start with "state_" and is merged with value of "item" variable. Whatever it is and we assume it produces the valid (existing) tags.
There cannot be any other in our Pirate language if there aren't such in original language. You can trust the programmers :)

Pirate English
look_at: Ahoy! Look at ${state_%{item}}.
state_sabre: a sharp saber
state_gun: a nice firearm

Examples
English
Hey! Look at a sharp sabre.
Hey! Look at a shiny pistol.

Pirate English
Ahoy! Look at a sharp saber.
Ahoy! Look at a nice firearm.

Another success, now something what our Pirate English will not cope with.

Switch field and inner tag field cooperation
============================================
The already presented features are enough for our Pirate English example, but it can't be denied that Pirate English
looks quite similar to English. All the difference in it is changing a few words, but some real languages are much more different.
I'm speaking about fusional languages. If you are not working with them, then you don't have to read further, but you may still find it interesting.
The following example will be much more complicated, but I hope I'll explain it precisely.
In Polish (and Russian, German... and many others), every noun has a grammatical form, specifying its gender.
Let's see: "szabla" (sabre) is feminine (f), while "pistolet" (pistol) is masculine (m).
This grammatical form is very important to set the correct suffix for adjectives describing the noun.
Let's see an example:
This is a new pistol. => To jest nowy pistolet.
This is a new sabre. => To jest nowa szabla.
"To jest" (This is) is the same for both items, but the suffix appended to stem "now" is based on the gender of the noun
("m" => "-y", "f" => "-a", "n" => "-e").

English
presentation_text: This is a new ${item_%{item_name}}.
item_sabre: sabre
item_pistol: pistol

I hope this part is quite easy. Using the same deduction as in the previous example we know that item_name can be only "sabre" or "pistol".
Now we need to prepare a translation for Polish.
We start with translating the items. It's possible to specify grammatical form for every tag so, we do it there:
item_sabre: szabla
form of item_sabre: f
item_pistol: pistolet
form of item_pistol: m

Okay, we have items, but there's the toughest part. At the first glance it should be something like:
presentation_text: To jest now%{WHAT:m?y|f?a|n?e} ${item_%{item_name}}.

What to set into "WHAT"? How can we guess what item is it? Should we ask a programmer to create a special variable which will contain the grammatical form?
It's a very bad idea, because there can be really many languages and programmer will most likely not understand most of
them and such requests would significantly complicate the translation process.
That's why there's a special way in which inner tag fields can cooperate with switch fields.

presentation_text: To jest now%{item_g:m?y|f?a|n?e} ${object_g:item_%{item_name}}.

That's right. We have specified an identifier for an inner tag ("object_g"),
which is then specified as an identifier of a variable which is looked in a switch field.
The inner tag's identifier specifies the grammatical form contained in an inner tag. It is then transported to switch which makes the correct decision.

So the full Polish translation looks like that:
presentation_text: To jest now%{item_g:m?y|f?a|n?e} ${object_g:item_%{item_name}}.
item_sabre: szabla
form of item_sabre: f
item_pistol: pistolet
form of item_pistol: m


If you don't need it and don't understand that - it's nothing to worry about. But if you are translating to a fusional language then I hope you have learned how does it work.

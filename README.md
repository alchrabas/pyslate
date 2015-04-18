pyslate - WORK IN PROGRESS, NOT TO BE USED YET
==============================================

A Python library for maintaining grammatically correct translations for multiple
languages.

What is it for?
---------------

As you probably know, there already are quite many i18n libraries for Python, mostly based on Gettext.
The reason I decided to prepare my own library was because I wasn't satisfied with any of them.
I needed full-features library, having similar capabilities as [Rails i18n](http://guides.rubyonrails.org/i18n.html). But it's not just a port.
I included all features I found important, but also many more:
 - i18n of text (tag values) based on their unique names (tag keys)
 - possibility to use different backends where translations are stored
 - support for special structures to use by translator directly in translation text
 - powerful fallback abilities in case that some variant of tag is missing
 - possibility injecting Python code into translations using decorators and custom functions
 - support for languages significantly different than English, based on practical knowledge and years of experience

Simple example
--------------

Define a translation file 'translations.json':
```json
{
    "hello_world": {
        "en": "Hello world!",
        "pl": "Witaj świecie!"
    }
}
```

Then you can check that it works in an interactive Python session:
```
>>> from pyslate import Pyslate, PyslateJsonBackend
>>> pys_en = Pyslate("en", backend=PyslateJsonBackend("translations.json"))
>>> pys_en.translate("hello_world")
Hello world!
>>> pys_pl = Pyslate("pl", backend=PyslateJsonBackend("translations.json"))
>>> pys_pl.translate("hello_world")
Witaj świecie!
```

It works!

So the most basic use it to create a pyslate object for a selected language and then request translation
of a specific tag using a `Pyslate.translate()` method. To make it more handy you can use `Pyslate.t` abbreviation. The JSON backend is used as an example, there are other storage options available.

More complicated example
------------------------

Change translation file into:
```json
{
    "introduction": {
        "en": "Hello! %{m?His|f?Her} name is %{name}."
    }
}
```
Then in your Python file you can write:
```
>>> pys.t("introduction", name="John", variant="m")
Hello! His name is John.
>>> pys.t("introduction", name="Judy", variant="f")
Hello! Her name is Judy.
```

There are two new things here: `%{name}` is a variable field where actual name (specified as a kwarg for `t()` method) is interpolated.
The second is `%{m?His|f?Her}` structure, called a switch field, which means:
if "variant" kwarg is "m", then print "His", if variant kwarg is "f" then print "Her". If none of these is true, then the first one is used as fallback.
It's easily possible to change pieces of translation based on context variables. That's great for English,
but it's often even more important for [fusional languages](https://en.wikipedia.org/wiki/Fusional_language) (like Polish) where word suffixes can vary in different forms.

Even more complicated example
-----------------------------

Change translation file into:
```json
{
    "show_off": {
        "en": "Hello! I'd like to show you ${toy@article}"
    },
    "toy": {
        "en": "wooden toy"
    }
}
```
Then you can write:
```
>>> pys.t("show_off")
Hello! I'd like to show you a wooden toy.
```

Two new things here: `${}` specifies an inner tag field. It means evaluating a "toy" tag and interpolating the contents directly into the main tag value.
At the end of the inner tag key there's a `@article`. It's a decorator, which means "take the tag value of tag it's used in, and then transform the string into something else".
Decorator "article" is included as specific for English and simply adds a/an article.
There also "upper" "lower" and "capitalize" decorators included right away. In addition, you can define any new decorator as you like.

Combo
-----

```json
{
    "show_off": {
        "en": "Hello! I'd like to show you ${%{toy_name}@article}"
    },
    "horse": {
        "en": "rocking horse"
    }
}
```
Then you can write:
```
>>> pys.t("show_off", toy_name="horse")
Hello! I'd like to show you a rocking horse.
```

How does it work? It's simply evaluating `%{toy_name}` variable field into "horse", which produces `%{horse@article}` inner tag field,
which is evaluated to "rocking horse" which is decorated using `article`, and in the end we get "a rocking horse".

Grammatical forms
-----------------

```json
{
    "announcement": {
        "en": "Hello! ${pol:%{policeperson}@article@capitalize} is here. %{pol:m?He|f?She} is going to help us.",
    },
    "john": {
        "en": ["policeman", "m"]
    },
    "judy": {
        "en": ["policewoman", "f"]
    }
}
```
Then you can write:
```
>>> pys.t("announcement", policeperson="john")
Hello! A policeman is here. He is going to help us.
```

For "john" key for English in specified JSON string there's a list instead of a single string.
The first element of the list is a value used for this key, the second is a grammatical form.

Another new thing is a "pol" identifier followed by a colon - both in an inner tag and a switch field.
The first is tag's ID, which then can be used to specify some special tag options (which will be explained later),
but it can also be used as identifier of grammatical form which can be used in switch field.
So, in short, "m" form is taken from an inner tag and used in switch field to print "He".
The use-case for such mechanism look quite slim for English, however it's very important in many languages,
where every noun has a grammatical form which can, for example, affect form of adjectives.

Tag variants
------------
It may happen that one tag is available in more than one form, which can for example mean different suffix based on
its context in the sentence. It's hard to be shown in English, so I'll put an example in Polish:
```json
{
    "having": {
        "en": "I have ${item_stone}.",
        "pl": "Mam ${item_stone}."
    },
    "not_having": {
        "en": "I don't have ${item_stone}",
        "pl": "Mam ${item_stone#g}"
    },
    "stone": {
        "en": "a stone",
        "pl": "kamień"
    },
    "stone#g": {
        "pl": "kamienia"
    }
}
```

```
>>> pys_en.t("not_having")
I don't have a stone.
>>> pys_pl.t("not_having")
Nie mam kamienia.
```
Let's take a look at the tag value of "not_having". In English it looks almost the same as "having",
but in Polish inner tag for item_stone has "#g" suffix, which makes it point at different tag. That is the tag's variant, whose value has different suffix.
What's the advantage of doing it instead of having own tag naming convention (e.g. "stone_g")?
The first thing is previously highlighted fallback ability. When some tag key contains variant which is unavailable in the database, then the more basic form is used.
That's why the most basic form (singular nominative) should be defined without any variant.
In case of lack of tag key and its basic form for a specified language, the tag or its base form is searched for in the fallback language.
Fallback mechanism is big and details can be found [here](). 
As you see, it's possible to adapt translations to the specified language without any programmer's knowledge what language is going to be introduced.
All can be managed in translation system by creating tags with correct variants.

Formatting numbers
------------------
When you translate number being an interpolated variable then you must decide if the used noun should be singular or plural.
Pyslate supports that easily by a special `number` variable:

```json
{
    "having_flower": {
        "en": "I have a flower",
    },
    "having_flower#p": {
        "en": "I have %{number} flowers",
    },
}
```

```
>>> pys.t("having_flower", number=1)
I have a flower.
>>> pys.t("having_flower", number=5)
I have 5 flowers.
```
These two forms are sufficient for English, but for many other languages it's not enough.
For example words can have different suffixes when there's a few of them and there's many of them.
In Polish there are three possibilities: singular (1), a few (2, 3, 4, 102, 103, 104...) and many (all the rest). 
The word "kwiat*ka*" (genitive form of "kwiat*ek*" ["a flower"]) has the following plural forms: "kwiatka", "kwiatki", "kwiatków".
```json
{
    "having_flower": {
        "pl": "Mam kwiatka",
    },
    "having_flower#e": {
        "pl": "Mam %{number} kwiatki.",
    },
    "having_flower#p": {
        "pl": "Mam %{number} kwiatków.",
    }
}
```
[(Every language can have different rules](http://unicode.org/repos/cldr-tmp/trunk/diff/supplemental/language_plural_rules.html),
so it's easy to configure them in `locales.py` file.

Custom functions
----------------
If none of previously mentioned options was a solution for your problem, then custom functions come to the reascue.
It's possible to create a meta-tag being in fact a custom python function which has access and can do almost everything then return a translated tag.
```json
{
    "product_presentation": {
        "en": "I'd like to present you a new product. It's ${product}.",
    },
    "car_personal": {
        "en": "a personal car"
    },
    "car_van": {
        "en": "a delivery van"
    },
    "product_template": {
        "en": "${type} produced by ${producer}"
    }
}
```
Then we have to create a custom function for a "product" inner tag field. Note this example can't be run by you in interactive shell,
as it features connecting to some imaginary database.

```
>>> def product_fun(helper, name, params):
>>>    product_id = params["product_id"]
>>>    product = db.Product.get(product_id)
>>>    if product.capacity >= 1000:
>>>        car_type = "car_van"
>>>    else:
>>>        car_type = "car_personal"
>>>    return helper.translate("product_template", type=car_type, producer=product.producer)
```

It gets kwarg argument "product_id", query the database for a product and print some data related to it.
Then it uses special helper object supplied by pyslate to translate a "product_template" tag, whose variable fields are set by data got inside of the function.
This way you can almost be sure that you'll never have to alter custom functions to make it work for some language.
In general, every custom function should return a string which is a value of this pseudo-tag.
Let's register that function:
```
>>> pys.register_function("product", product_fun)
```
Now let's assume the product with id 7 is a product with capacity 2000 produced by Audi.
```
>>> pys.t("product_presentation", product_id=7)
I'd like to present you a new product. It's a delivery van produced by Audi.
```
It works great.
Please note if you need lots of custom functions in your code, then maybe any i18n library isn't a correct solution for your kind of problem.
You shouldn't also misuse Pyslate as a templating designer, because any real (like jinja2) would do it better.

Integration with templating engines
-----------------------------------
Most likely your application uses some template system to separate logic from the presentation.
As there are probably lots of static messages in your template files that need to be translated, then you need a way to
call pyslate directly from it.
Considering short tags and easy API it's very simple to integrate with template languages.
I'll show how to get Pyslate work with Flask-Jinja2, but it's just as easy for any other templating language which allows defining custom functions.

Flask-Jinja2 integration
========================
`app.jinja_env.globals` contains the dict of all global variables of jinja2 being used by flask application `app`.
So all you need to do, assuming variable `pyslate` holds instance of class Pyslate is:
```
app.jinja_env.globals.update(t=lambda *args, **kwargs: pyslate.t(*args, **kwargs))
```
It registers a "t" function which is a lambda passing all the translations to pyslate object.
Does the one below work too? 
```
app.jinja_env.globals.update(t=pyslate.t)
app.jinja_env.globals.update(l=pyslate.l)
```


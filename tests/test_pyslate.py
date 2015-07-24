# encoding: utf-8
import unittest
import datetime
from pyslate.config import DefaultConfig
from pyslate.parser import PyslateException
from pyslate.pyslate import Pyslate


class Item:
    def __init__(self, item_id, name, quality=0):
        self.item_id = item_id
        self.name = name
        self.quality = quality


def get_quality_tag(quality):
    if quality > 5:
        return "a_masterwork"
    else:
        return "a_poor"


def obj_fun(helper, name, params):
    item_name = params["item_name"]  # fallback which must always be available
    quality_tag = ""
    form = ""
    case = ""

    if "#" in name:
        case += name.partition("#")[2]

    if "item" in params and params["item"]:
        item_name = params["item"].name
        quality_tag = get_quality_tag(params["item"].quality)
        form = helper.form("entity_" + item_name) if helper.form("entity_" + item_name) else ""

    form += case

    if quality_tag:
        quality_tag = "${" + quality_tag + ("#" + form if form else "") + "} "

    return quality_tag + "${entity_" + item_name + ("#" + case if case else "") + "}"


class BackendStub():

    def get_content(self, tag_names, languages):
        for language in languages:
            for tag_name in tag_names:
                if language in BackendStub.TAGS.get(tag_name, {}):
                    return BackendStub.TAGS[tag_name][language]
        return None

    def get_form(self, tag_names, languages):
        for language in languages:
            for tag_name in tag_names:
                if language in BackendStub.TAGS.get(tag_name, {}):
                    if "form" in BackendStub.TAGS[tag_name] and language in BackendStub.TAGS[tag_name]["form"]:
                        return BackendStub.TAGS[tag_name]["form"][language]
                    else:
                        return None

    # region constants
    TAGS = {
        "hello_world": {
            "en": "Hello world",
            "pl": "Witaj swiecie",
        },
        "welcome": {
            "en": "Welcome!",
        },
        "my_name": {
            "en": "My name is %{name}",
        },
        "item_ownership": {
            "en": "${welcome} I have ${entity_%{item_name}#u}.",
        },
        "entity_sword": {
            "en": "a sword",
            "pl": "miecz",
        },
        "entity_sword#p": {
            "en": "%{number} swords",
        },
        "entity_sword#u": {
            "en": "swords",
        },
        "entity_sword#a": {
            "pl": "miecza",
        },
        "entity_stone": {
            "en": "a block of stone",
            "pl": "bryła kamienia",
        },
        "entity_stone#p": {  # plural = many
            "en": "%{number} blocks of stone",
            "pl": "%{number} brył kamieni",
        },
        "entity_stone#w": {  # a few
            "pl": "%{number} bryły kamieni",
        },
        "entity_stone#u": {  # undefined
            "en": "some stone",
            "pl": "trochę kamieni",
        },
        "entity_carrot": {
            "en": "a carrot",
            "pl": "marchewka",
        },
        "entity_carrot#p": {  # many
            "en": "%{number} carrots",
            "pl": "%{number} marchewek",
        },
        "entity_carrot#w": {  # a few
            "pl": "%{number} marchewki",
        },
        "entity_carrot#u": {  # undefined
            "en": "some carrots",
            "pl": "trochę marchewek",
        },
        "entity_beetroot": {
            "en": "beetroot%{tag_v:s?|p?s}",
            "pl": "%{number} burak%{tag_v:s?|w?i|p?ów}",
        },
        "action_give_others": {
            "en": "You see ${giver:char_info} give ${entity_%{item_name}#u} to ${taker:char_info}.",
        },
        "action_give_giver": {
            "en": "You give ${object_info} to ${char_info}.",
        },
        "hunting_hunter": {
            "en": "You attack ${entity_%{animal}@article} using ${entity_%{item_name}}.",
            "pl": "Atakujesz ${entity_%{animal}#a} przy pomocy ${entity_%{item_name}#a}.",
        },
        "entity_elk": {
            "en": "elk",
            "pl": "łoś",
        },
        "entity_elk#a": {
            "pl": "łosia",
        },
        "entity_elk#pa": {
            "pl": "łosie",
        },
        "entity_hammer": {
            "en": "hammer",
            "pl": "młotek",
        },
        "a_masterwork": {
            "en": "a masterwork",
            "pl": "wspaniale wykonany",
        },
        "a_masterwork#f": {
            "pl": "wspaniale wykonana",
        },
        "a_poor": {
            "en": "a poor",
            "pl": "kiepski",
        },
        "a_poor#f": {
            "pl": "kiepska",
        },
        "a_poor#mg": {
            "pl": "kiepskiego",
        },
        "entity_wand": {
            "en": "wand",
            "pl": "różdżka",
            "form": {
                "en": "c",
                "pl": "f",
            }
        },
        "being_in_shop": {
            "en": "I was in shop",
            "pl": "Był%{m?em|f?am} dziś w sklepie",
        },
        "talking_the_same": {
            "en": "I told %{sb:m?him|f?her} it's stupid and %{sb:m?|f?s}he told me the same.",
            "pl": "Powiedział%{me:m?em|f?am} %{sb:m?mu|f?jej}, że to głupie, a on%{sb:m?|f?a} powiedział%{sb:m?|f?a} mi to samo.",
        },
        "talking_the_same2": {
            "en": "I told ${sb:form_him} it's stupid and %{sb:suffix_he} told me the same.",
            "pl": "Powiedział${suffix_em#%{me}} ${form_him#%{sb}}, że to głupie, a ${form_he#%{sb}} powiedział${suffix_did_form#%{sb}} mi to samo.",
        },
        # region helpers needed for variants emulation
        "suffix_em#f": {
            "pl": "am",
        },
        "suffix_em#m": {
            "pl": "em",
        },
        "form_him#f": {
            "pl": "jej",
        },
        "form_him#m": {
            "pl": "mu",
        },
        "form_he#f": {
            "pl": "ona",
        },
        "form_he#m": {
            "pl": "on",
        },
        "suffix_did_form#f": {
            "pl": "a",
        },
        "suffix_did_form#m": {
            "pl": "",
        },
        # endregion helpers needed for variants emulation
        "buying_the_pizza": {
            "en": "I've bought the pizza.",
            "pl": "Kupił%{tag_v:m?e|f?a}m pizzę.",
        },
        "missing_placeholder": {
            "pl": "lala %{hehe}",
        },
        "missing_tag": {
            "pl": "lala ${hehe}",
        },
        "event_hit_others": {
            "pl": "Widzisz, że ${attacker:char_info} uderzył%{attacker:m?|f?a} ${victim:char_info}.",
        },
        "event_hit_others_weapon": {
            "pl": "Widzisz, że ${attacker:char_info} uderzył%{attacker:m?|f?a} ${victim:char_info} używając ${object_info#g}.",
        },
        "info_victim": {
            "pl": "Ofiara wypadku to %{victim:f?kobieta|m?mężczyzna}.",
        },
        "entity_doughroller": {
            "pl": "wałek",
            "form": {
                "pl": "m",
            }
        },
        "char_victim": {
            "pl": "${tajnosc} Jest %{victim:x?[NO DATA]|f?fajna|m?fajny|n?fajne}.",
        },
        "char_victim2": {
            "pl": "${victim:fun_tajnosc} Jest %{victim:x?[NO DATA]|f?fajna|m?fajny|n?fajne}.",
        },
        "tajnosc": {
            "pl": "Zniszczono %{victim:f?nową|m?nowy|n?nowe} ${victim:entity_%{item_name}}.",
        },
        "entity_doughroller#g": {
            "pl": "wałka",
            "form": {
                "pl": "m",
            }
        },
        "doing_this_cookie": {
            "pl": "Zrobiłem %{cookie:x?temu|p?tym} ciasteczk%{cookie:x?o|g?om}.",
        },
    }
    # endregion
    """

    -- plural forms
    ->  [empty] - 1             np. 1 carrot,     1 marchewka
        z - zero [0]            np. 0 carrots,    0 marchewek
        t - two [2]             np. 2 carrots,    2 marchewki
        w - a feW [2,4]         np. 3 carrots,    3 marchewki
    ->  y - manY 5+             np. 5 carrots,    5 marchewek
        u - undefined           np. carrots|some carrots, marchewki|trochę marchewek
        p - other e.g. 1.5      np. 4.5 carrots,  4.5 marchewki

    -- noun cases
    ->  [empty]  - nominative (mianownik)   np. miecz
        g - genitive (dopełniacz)           np. miecza
        d - dative (celownik)               np. mieczowi
    ->  a - accusative (biernik)            np. miecz
        b - ablative (narzędnik)            np. mieczem
        l - locative (miejscownik)          np. mieczu
        v - vocative (wołacz)               np. mieczu

    --gender forms
    m, f, n


    mnf - gender
    gdablv - cases
    sztwyuop - numbers

    cehijkqrxy - not used

    Kupił%{gender:m?eś|f?aś} nowiutk{item_g:m?i|f?ą|p?ie} ${entity_${item_name}}. # no dobra, to się nie może zdarzyć


    You attack an elk.

    entity_elk: elk
    entity_elk#a: %{|an?an} elk   variant=an

    entity_elk: ło{n?ś|a?sia}

    Spotykasz ${animal:entity_%{animal}#a}, a następnie atakujesz %{animal:gen_he#a}









    """


class TestTranslationsEnglish(unittest.TestCase):

    def setUp(self):
        self.pys = Pyslate("en", BackendStub())

    def test_simple(self):
        # pl translation is available so it should be used
        self.assertEqual("Hello world", self.pys.t("hello_world"))

        # no pl translation is available, so it should fallback to en
        self.assertEqual("Welcome!", self.pys.t("welcome"))

    def test_numbers(self):
        self.assertEqual("10 carrots", self.pys.t("entity_carrot#p", number=10))
        self.assertEqual("10 carrots", self.pys.t("entity_carrot", number=10))
        self.assertEqual("4 carrots", self.pys.t("entity_carrot", number=4))
        self.assertEqual("a carrot", self.pys.t("entity_carrot", number=1))
        self.assertEqual("1.3 carrots", self.pys.t("entity_carrot", number=1.3))

    def test_replacement(self):  # using a variant specified in a function
        self.assertEqual("Welcome! I have swords.", self.pys.t("item_ownership", item_name="sword"))

    def test_recursion(self):  # complicated example of using custom functions
        self.pys.register_function("char_info",
                                   lambda helper, name, params: "John" if params['char_id'] == 1 else "Edd")
        self.assertEqual("You see John give some carrots to Edd.",
                         self.pys.t("action_give_others", item_name="carrot", groups={"giver": {"char_id": 1},
                                                                                      "taker": {"char_id": 2},
                                                                                      }))

    def test_recursion_fun(self):
        self.pys.register_function("object_info",
                                   lambda helper, name, params: "a note 'trololo'" if params['item_id'] == 3 else "ERR")
        self.pys.register_function("char_info",
                                   lambda helper, name, params: "Edd" if params['char_id'] == 2 else "John")
        self.assertEqual("You give a note 'trololo' to Edd.", self.pys.t("action_give_giver", item_id=3, char_id=2))

    def test_hunt(self):
        self.assertEqual("You attack an elk using a sword.",
                         self.pys.t("hunting_hunter", animal="elk", item_name="sword"))

    def test_decorator(self):  # using one of already included decorators
        self.assertEqual("WELCOME! I HAVE SWORDS.", self.pys.t("item_ownership@upper", item_name="sword"))

    def test_deterministic_function(self):  # deterministic funs are run once and result of their execution is memorized

        calls_count = [0]

        def fun(helper, tag_name, params):
            calls_count[0] += 1
            return ":)"

        self.pys.register_function("fun", fun, is_deterministic=True)

        self.assertEqual(":)", self.pys.t("fun"))
        self.assertEqual(":)", self.pys.t("fun"))
        self.assertEqual(":)", self.pys.t("fun"))

        self.assertEqual(1, calls_count[0])  # make sure that function was called just once

    def test_localization(self):  # en = en_GB
        # date
        self.assertEqual("1999-12-15", self.pys.l(datetime.date(1999, 12, 15)))
        self.assertEqual("2222-11-1", self.pys.l(datetime.date(2222, 11, 1)))
        self.assertEqual("1900-1-3", self.pys.l(datetime.date(1900, 1, 3)))

        # time
        self.assertEqual("2:11:37 AM", self.pys.l(datetime.time(2, 11, 37)))
        self.assertEqual("6:13:22 PM", self.pys.l(datetime.time(18, 13, 22)))

        # datetime
        self.assertEqual("1999-12-7, 2:11:37 AM", self.pys.l(datetime.datetime(1999, 12, 7, 2, 11, 37)))
        self.assertEqual("2128-1-3, 6:13:22 PM", self.pys.l(datetime.datetime(2128, 1, 3, 18, 13, 22)))


class TestTranslationsPolish(unittest.TestCase):

    def setUp(self):
        self.pys = Pyslate("pl", BackendStub())
        self.pys.fallbacks["pl"] = "en"  # it's not necessary

    def test_numbers(self):
        self.assertEqual("10 marchewek", self.pys.t("entity_carrot#p", number=10))
        self.assertEqual("10 marchewek", self.pys.t("entity_carrot", number=10))
        self.assertEqual("4 marchewki", self.pys.t("entity_carrot", number=4))
        self.assertEqual("marchewka", self.pys.t("entity_carrot", number=1))
        self.assertEqual("1,5 marchewek", self.pys.t("entity_carrot", number=1.5))  # might need polishing

    def test_numbers_variants(self):
        self.assertEqual("10 buraków", self.pys.t("entity_beetroot#p", number=10))
        self.assertEqual("10 buraków", self.pys.t("entity_beetroot", number=10))
        self.assertEqual("4 buraki", self.pys.t("entity_beetroot", number=4))
        self.assertEqual("1 burak", self.pys.t("entity_beetroot", number=1))
        self.assertEqual("1,5 buraków", self.pys.t("entity_beetroot", number=1.5))

    def test_hunt(self):
        self.assertEqual("Atakujesz łosia przy pomocy miecza.",
                         self.pys.t("hunting_hunter", animal="elk", item_name="sword"))

    def test_decorators(self):
        # decorators are

        def pokemon(value):
            res = ""
            for char_pos in range(len(value)):
                res += value[char_pos].upper() if char_pos % 2 == 0 else value[char_pos]
            return res

        def add_dots(value):
            return "".join([char + "." for char in value])

        self.pys.register_decorator("pokemon", pokemon)
        self.pys.register_decorator("add_dots", add_dots)

        self.assertEqual("miecz", self.pys.t("entity_sword"))
        self.assertEqual("Miecz", self.pys.t("entity_sword@capitalize"))
        self.assertEqual("MIECZ", self.pys.t("entity_sword@upper"))
        self.assertEqual("M.i.E.c.Z.", self.pys.t("entity_sword@pokemon@add_dots"))

    def test_decorators_and_functions(self):  # funs and decorators use the same namespace, so they overwrite each other

        self.pys.register_decorator("capitalize", str.capitalize)
        self.pys.register_function("capitalize",
                                   lambda helper, name, params: helper.translation("entity_sword").capitalize())
        # decorator should now be overwritten

        self.assertEqual("Miecz", self.pys.t("capitalize"))
        with self.assertRaises(PyslateException):
            self.pys.t("entity_sword@capitalize")  # decorator no longer exists

    def test_language_specific_decorator(self):  # trying to use decorator which is available thanks to fallback rules

        self.assertEqual("a miecz", self.pys.t("entity_sword@article"))

        self.pys.register_decorator("strlen", lambda x: str(len(x)), language="es")
        with self.assertRaises(PyslateException):
            self.pys.t("entity_sword@strlen")


    def test_detailed_function(self):  # function allows for a special behaviour when you call it like a tag
        self.pys.register_function("object_info", obj_fun)

        self.assertEqual("wspaniale wykonany młotek",
                         self.pys.t("object_info", item=Item(1, "hammer", quality=10), item_name="hammer"))

        self.assertEqual("wspaniale wykonana różdżka",
                         self.pys.t("object_info", item=Item(2, "wand", quality=10), item_name="wand"))

        self.assertEqual("kiepski młotek",
                         self.pys.t("object_info", item=Item(3, "hammer", quality=3), item_name="hammer"))

        self.assertEqual("różdżka",
                         self.pys.t("object_info", item=None, item_name="wand"))  # fallback

    def test_switch_field(self):  # for fusional languages (e.g. slavic) the suffix is often based on grammatical gender

        self.assertEqual("Byłem dziś w sklepie",
                         self.pys.t("being_in_shop", variant="m"))

        self.assertEqual("Byłam dziś w sklepie",
                         self.pys.t("being_in_shop", variant="f"))

        self.assertEqual("Byłem dziś w sklepie",
                         self.pys.t("being_in_shop", variant="yeti"))

        self.assertEqual("Powiedziałam mu, że to głupie, a on powiedział mi to samo.",
                         self.pys.t("talking_the_same", me="f", sb="m"))

        self.assertEqual("Powiedziałam jej, że to głupie, a ona powiedziała mi to samo.",
                         self.pys.t("talking_the_same", me="f", sb="f"))

        self.assertEqual("Powiedziałem mu, że to głupie, a on powiedział mi to samo.",
                         self.pys.t("talking_the_same", me="m", sb="m"))

    def test_switch_field_default(self):  # if there's no matching key in switch, then use first-left one
        self.assertEqual("Powiedziałem mu, że to głupie, a on powiedział mi to samo.",
                         self.pys.t("talking_the_same"))

        self.assertEqual("Powiedziałam mu, że to głupie, a on powiedział mi to samo.",
                         self.pys.t("talking_the_same", me="f"))

        self.assertEqual("Powiedziałem jej, że to głupie, a ona powiedziała mi to samo.",
                         self.pys.t("talking_the_same", me="Xd", sb="f"))

    def test_switch_field_emulation(self):  # there's example of how to emulate switch-fields behaviour (very verbose)
        self.assertEqual("Powiedziałem mu, że to głupie, a on powiedział mi to samo.",
                         self.pys.t("talking_the_same2", me="m", sb="m"))

        self.assertEqual("Powiedziałem jej, że to głupie, a ona powiedziała mi to samo.",
                         self.pys.t("talking_the_same2", me="m", sb="f"))

        self.assertEqual("Powiedziałam jej, że to głupie, a ona powiedziała mi to samo.",
                         self.pys.t("talking_the_same2", me="f", sb="f"))

    def test_switch_field_contained(self):
        self.assertEqual("Zrobiłem tym ciasteczkom.", self.pys.t("doing_this_cookie", cookie="pg"))
        self.assertEqual("Zrobiłem tym ciasteczko.", self.pys.t("doing_this_cookie", cookie="p"))
        self.assertEqual("Zrobiłem temu ciasteczkom.", self.pys.t("doing_this_cookie", cookie="g"))
        self.assertEqual("Zrobiłem temu ciasteczko.", self.pys.t("doing_this_cookie", cookie=""))

    # sometimes switch variant is based on form taken from inner tag
    def test_switch_field_with_grammatical_form_from_inner_tag(self):
        def char_info(helper, name, params):
            char_name = "Rysiek" if params["char_id"] == 1 else "Grażyna"
            helper.return_form("m" if char_name == "Rysiek" else "f")
            return char_name

        self.pys.register_function("char_info", char_info)

        self.assertEqual("Widzisz, że Rysiek uderzył Grażyna.",
                         self.pys.t("event_hit_others", groups={"attacker": {"char_id": 1}, "victim": {"char_id": 3}}))

        self.assertEqual("Widzisz, że Grażyna uderzyła Rysiek.",
                         self.pys.t("event_hit_others", groups={"attacker": {"char_id": 3}, "victim": {"char_id": 1}}))

        self.pys.register_function("object_info", obj_fun)

        self.assertEqual("Widzisz, że Grażyna uderzyła Rysiek używając kiepskiego wałka.",
                         self.pys.t("event_hit_others_weapon", groups={"attacker": {"char_id": 3}, "victim": {"char_id": 1}},
                                    item=Item(13, "doughroller", quality=2), item_name="doughroller"))

        # "f" should be default, but it may be overwritten by the variant tag in the test above
        # in case of incorrect implementation that uses global context
        self.assertEqual("Ofiara wypadku to kobieta.", self.pys.t("info_victim"))
        self.assertEqual("Ofiara wypadku to mężczyzna.", self.pys.t("info_victim", victim="m"))

        # it should be IMPOSSIBLE to get form from context of its inner tag, because it's local to InnerTagField
        self.assertEqual("Zniszczono nowy wałek. Jest [NO DATA].", self.pys.t("char_victim", item_name="doughroller"))

    # correct way of doing the example from above is to use a custom function
    # which returns the grammatical form for a specific item
    def test_variants_with_form_from_inner_tag_by_function(self):

        def fun_tajnosc(helper, name, params):
            text = helper.translation("tajnosc", **params)
            item_form = helper.form("entity_" + params["item_name"])

            helper.return_form(item_form)
            return text

        self.pys.register_function("fun_tajnosc", fun_tajnosc)
        self.assertEqual("Zniszczono nowy wałek. Jest fajny.", self.pys.t("char_victim2", item_name="doughroller"))

    def test_tag_variant(self):
        self.assertEqual("Kupiłem pizzę.",
                         self.pys.t("buying_the_pizza#m"))

        self.assertEqual("Kupiłam pizzę.",
                         self.pys.t("buying_the_pizza#f"))

        self.assertEqual("Kupiłem pizzę.",
                         self.pys.t("buying_the_pizza"))

    # that's what should happen when there's no required base tag in this or in fallback language
    def test_missing_tag(self):
        self.assertEqual("lala [MISSING VALUE FOR 'hehe']",
                         self.pys.t("missing_placeholder"))

        self.assertEqual("lala [MISSING TAG 'hehe']",
                         self.pys.t("missing_tag"))

    def test_localization(self):
        self.assertEqual("15.12.1999", self.pys.l(datetime.date(1999, 12, 15)))
        self.assertEqual("1.11.2222", self.pys.l(datetime.date(2222, 11, 1)))
        self.assertEqual("2.01.1900", self.pys.l(datetime.date(1900, 1, 2)))

        self.assertEqual("2:11:37", self.pys.l(datetime.time(2, 11, 37)))
        self.assertEqual("18:13:22", self.pys.l(datetime.time(18, 13, 22)))

        self.assertEqual("7.12.1999, 2:11:37", self.pys.l(datetime.datetime(1999, 12, 7, 2, 11, 37)))
        self.assertEqual("3.01.2128, 18:13:22", self.pys.l(datetime.datetime(2128, 1, 3, 18, 13, 22)))


class TestConfigPolishTranslations(unittest.TestCase):

    def test_no_inner_tags(self):
        config = DefaultConfig()
        config.ALLOW_INNER_TAGS = False
        self.pys = Pyslate("pl", backend=BackendStub(), config=config)

        self.assertEqual("${welcome} I have ${entity_sword#u}.",
                         self.pys.t("item_ownership", item_name="sword"))


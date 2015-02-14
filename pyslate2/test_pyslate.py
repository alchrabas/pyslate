import unittest
from pyslate2.pyslate import Pyslate


class BackendStub():

    def get_content(self, tag_names, languages):
        for language in languages:
            for tag_name in tag_names:
                if language in BackendStub.TAGS.get(tag_name, {}):
                    return BackendStub.TAGS[tag_name][language]
        return None

    def get_grammar(self, tag_names, languages):
        for language in languages:
            for tag_name in tag_names:
                if language in BackendStub.TAGS.get(tag_name, {}):
                    if "grammar" in BackendStub.TAGS[tag_name] and language in BackendStub.TAGS[tag_name]["grammar"]:
                        return BackendStub.TAGS[tag_name]["grammar"][language]
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
            "en": "${welcome} I have ${entity_%{item_name}#p}.",
        },
        "entity_sword": {
            "en": "a sword",
        },
        "entity_sword#m": {
            "en": "%{number} swords",
        },
        "entity_sword#p": {
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
        "entity_stone#f": {  # a few
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
        "entity_carrot#m": {  # many
            "en": "%{number} carrots",
            "pl": "%{number} marchewek",
        },
        "entity_carrot#f": {  # a few
            "pl": "%{number} marchewki",
        },
        "entity_carrot#u": {  # undefined
            "en": "some carrots",
            "pl": "trochę marchewek",
        },
        "entity_carrot#o": {  # other
            "pl": "%{number} marchewki",
        },
        "entity_beetroot": {
            "en": "beetroot%{tag_v:s?|m?s}",
            "pl": "%{number} burak%{tag_v:s?|f?i|m?ów|o?a}",
        },
        "action_give_others": {
            "en": "You see ${giver:char_info} give ${entity_%{item_name}#u} to ${taker:char_info}.",
        },
        "action_give_giver": {
            "en": "You give ${object_info} to ${char_info}.",
        },
        "hunting_hunter": {
            "en": "You attack ${entity_%{animal}} using ${entity_%{item_name}}.",
            "pl": "Atakujesz ${entity_%{animal}#a} przy pomocy ${entity_%{item_name}#a}.",
        },
        "entity_elk": {
            "en": "an elk",
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
        "entity_wand": {
            "en": "wand",
            "pl": "różdżka",
            "grammar": {
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


    }
    # endregion
    """

    -- odmiana liczby mnogiej

    ->  [empty] - 1             np. 1 marchewka
        f - a few [2,4]         np. 3 marchewki
    ->  m - 5+                  np. 5 marchewek
        u - undefined           np. trochę karchewek
        o - other e.g. 1.5      np. 4.5 marchewki
    ->  p - bez określonego     np. marchewki

    -- odmiana przedmiotów

    ->  [empty]  - nominative (mianownik)  np. miecz
        g - genitiv (dopełniacz)           np. miecza
        d - dativ (celownik)               np. mieczowi
    ->  a - accusative (biernik)           np. miecz
        b - ablative (narzędnik)           np. mieczem
        l - locative (miejscownik)         np. mieczu
        v - vocative (wołacz)              np. mieczu


    Kupił%{gender:m?eś|f?aś} nowiutk{item_g:m?i|f?ą|p?ie} ${entity_${item_name}}. # no dobra, to się nie może zdarzyć


    You have bought a%{item:v?n|} ${item:entity_%{item_name}}. item_name="apron"
    entity_apron

    Wersja skrócona, bazuje na z góry określonym argumencie kluczowym "variant":
    Kupił%{m?eś|f?aś}


    You attack an elk.

    entity_elk: elk
    entity_elk#a: %{|an?an} elk   variant=an

    entity_elk: ło{n?ś|a?sia}

    Spotykasz ${animal:entity_%{animal}#a}, a następnie atakujesz %{animal:gen_he#a}









    """


class TestTranslationsEnglish(unittest.TestCase):

    def setUp(self):
        self.pys = Pyslate("en", BackendStub())
        self.pys.set_fallback_language("en", "en")

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

    def test_replacement(self):
        self.assertEqual("Welcome! I have swords.", self.pys.t("item_ownership", item_name="sword"))

    def test_recursion(self):
        self.pys.register_function("char_info", lambda self, name, params: "John" if params['char_id'] == 1 else "Edd")
        self.assertEqual("You see John give some carrots to Edd.",
                         self.pys.t("action_give_others", item_name="carrot", groups={"giver": {"char_id": 1},
                                                                                      "taker": {"char_id": 2},
                                                                                      }))

    def test_recursion_fun(self):
        self.pys.register_function("object_info", lambda self, name, params: "a note 'trololo'" if params['item_id'] == 3 else "ERROR")
        self.pys.register_function("char_info", lambda self, name, params: "Edd" if params['char_id'] == 2 else "John")
        self.assertEqual("You give a note 'trololo' to Edd.", self.pys.t("action_give_giver", item_id=3, char_id=2))

    def test_hunt(self):
        self.assertEqual("You attack an elk using a sword.",
                         self.pys.t("hunting_hunter", animal="elk", item_name="sword"))


class TestTranslationsPolish(unittest.TestCase):

    def setUp(self):
        self.pys = Pyslate("pl", BackendStub())
        self.pys.set_fallback_language("pl", "en")  # it should be unnecessary

    def test_numbers(self):
        self.assertEqual("10 marchewek", self.pys.t("entity_carrot#m", number=10))
        self.assertEqual("10 marchewek", self.pys.t("entity_carrot", number=10))
        self.assertEqual("4 marchewki", self.pys.t("entity_carrot", number=4))
        self.assertEqual("marchewka", self.pys.t("entity_carrot", number=1))
        self.assertEqual("1,5 marchewki", self.pys.t("entity_carrot", number=1.5))

    def test_numbers_variants(self):
        self.assertEqual("10 buraków", self.pys.t("entity_beetroot#m", number=10))
        self.assertEqual("10 buraków", self.pys.t("entity_beetroot", number=10))
        self.assertEqual("4 buraki", self.pys.t("entity_beetroot", number=4))
        self.assertEqual("1 burak", self.pys.t("entity_beetroot", number=1))
        self.assertEqual("1,5 buraka", self.pys.t("entity_beetroot", number=1.5))

    def test_hunt(self):
        self.assertEqual("Atakujesz łosia przy pomocy miecza.",
                         self.pys.t("hunting_hunter", animal="elk", item_name="sword"))

    def test_detailed_function(self):

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

        def obj_fun(s, name, params):
            item_name = params["item_name"]  # fallback which must always be available
            quality_tag = ""
            grammar = ""
            if "item" in params and params["item"]:
                item_name = params["item"].name
                quality_tag = get_quality_tag(params["item"].quality)
                grammar = s._get_raw_grammar("entity_" + item_name)

            if quality_tag:
                quality_tag = "${" + quality_tag + ("#" + grammar if grammar else "") + "} "

            return quality_tag + "${entity_" + item_name + "}"

        self.pys.register_function("object_info", obj_fun)

        self.assertEqual("wspaniale wykonany młotek",
                         self.pys.t("object_info", item=Item(1, "hammer", quality=10), item_name="hammer"))

        self.assertEqual("wspaniale wykonana różdżka",
                         self.pys.t("object_info", item=Item(2, "wand", quality=10), item_name="wand"))

        self.assertEqual("kiepski młotek",
                         self.pys.t("object_info", item=Item(3, "hammer", quality=3), item_name="hammer"))


        self.assertEqual("różdżka",
                         self.pys.t("object_info", item=None, item_name="wand"))  # fallback

    def test_variants(self):

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

    def test_variants_default(self): # use first left key from variants tag
        self.assertEqual("Powiedziałem mu, że to głupie, a on powiedział mi to samo.",
                         self.pys.t("talking_the_same"))

        self.assertEqual("Powiedziałam mu, że to głupie, a on powiedział mi to samo.",
                         self.pys.t("talking_the_same", me="f"))

        self.assertEqual("Powiedziałem jej, że to głupie, a ona powiedziała mi to samo.",
                         self.pys.t("talking_the_same", me="Xd", sb="f"))

    def test_variants_emulation(self):
        self.assertEqual("Powiedziałem mu, że to głupie, a on powiedział mi to samo.",
                         self.pys.t("talking_the_same2", me="m", sb="m"))

        self.assertEqual("Powiedziałem jej, że to głupie, a ona powiedziała mi to samo.",
                         self.pys.t("talking_the_same2", me="m", sb="f"))

        self.assertEqual("Powiedziałam jej, że to głupie, a ona powiedziała mi to samo.",
                         self.pys.t("talking_the_same2", me="f", sb="f"))

    def test_tag_variant(self):
        self.assertEqual("Kupiłem pizzę.",
                         self.pys.t("buying_the_pizza#m"))

        self.assertEqual("Kupiłam pizzę.",
                         self.pys.t("buying_the_pizza#f"))

        self.assertEqual("Kupiłem pizzę.",
                         self.pys.t("buying_the_pizza"))

    def test_missing_tag(self):
        self.assertEqual("lala [MISSING VALUE FOR 'hehe']",
                         self.pys.t("missing_placeholder"))

        self.assertEqual("lala [MISSING TAG 'hehe']",
                         self.pys.t("missing_tag"))
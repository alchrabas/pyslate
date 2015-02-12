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
        "entity_sword#p": {
            "en": "${number} swords",
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
        "entity_carrot#p": {  # plural = many
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
            "en": "${number} of a carrot",
            "pl": "${number} marchewki",
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
            "pl": "Był%{m>em|f>am} dziś w sklepie",
        },
    }
    # endregion
    """

    [empty] - 1
    f - a few [2,4]
    p - 5+
    u - undefined
    o - other e.g. 1.5

    -- odmiana przedmiotów

    [empty]  - nominative (mianownik)
    a - accusative (biernik)


    Kupił%{gender:m>eś|f>aś} nowiutk{item_g:m>i|f>ą|p>ie} ${entity_${item_name}}. # no dobra, to się nie może zdarzyć


    You have bought a%{item:v>n|} ${item:entity_%{item_name}}. item_name="apron"
    entity_apron

    Wersja skrócona, bazuje na określonym argumencie kluczowym "variant":
    Kupił%{m>eś|f>aś}


    You attack an elk.

    entity_elk: elk
    entity_elk#a: %{an>an|}elk   variant=an

    entity_elk: ło{n>ś|a>sia}

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

    def test_replacement(self):
        self.assertEqual("Welcome! I have  swords.", self.pys.t("item_ownership", item_name="sword"))

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
        self.pys.set_fallback_language("pl", "en") # it should be unnecessary

    def test_numbers(self):
        self.assertEqual("10 marchewek", self.pys.t("entity_carrot#p", number=10))
        self.assertEqual("10 marchewek", self.pys.t("entity_carrot", number=10))
        self.assertEqual("4 marchewki", self.pys.t("entity_carrot", number=4))
        self.assertEqual("marchewka", self.pys.t("entity_carrot", number=1))

    def test_hunt(self):
        self.assertEqual("Atakujesz łosia przy pomocy miecza.",
                         self.pys.t("hunting_hunter", animal="elk", item_name="sword"))

    def test_detailed_function(self):

        class Item:

            def __init__(self, item_id, name):
                self.item_id = item_id
                self.name = name

            def get_id(self):
                return self.item_id

            def get_name(self):
                return self.name

        def get_deter(quality):
            if quality > 5:
                return "a_masterwork"
            else:
                return "a_poor"

        def obj_fun(s, name, params):
            item_name = params["item_name"]  # fallback which must always be available
            if "item" in params and params["item"]:
                item_name = params["item"].get_name()
            q = get_deter(params["quality"])
            grammar = s._get_raw_grammar("entity_" + item_name)
            if grammar:
                q += "#" + grammar

            return "${" + q + "} ${entity_" + item_name + "}"

        self.pys.register_function("object_info", obj_fun)

        self.assertEqual("wspaniale wykonany młotek",
                         self.pys.t("object_info", item=Item(1, "hammer"), item_name="hammer", quality=10))

        self.assertEqual("wspaniale wykonana różdżka",
                         self.pys.t("object_info", item=Item(2, "wand"), item_name="wand", quality=10))

    def test_variants(self):

        self.assertEqual("Byłem dziś w sklepie",
                         self.pys.t("being_in_shop", variant="m"))

        self.assertEqual("Byłam dziś w sklepie",
                         self.pys.t("being_in_shop", variant="f"))

        self.assertEqual("Byłem dziś w sklepie",
                         self.pys.t("being_in_shop", variant="yeti"))
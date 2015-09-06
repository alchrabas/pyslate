# encoding: utf-8

import unittest
from pyslate.parser import PyLexer, PyParser, InnerTagField, VariableField, SwitchField, PyslateException


class LexerTest(unittest.TestCase):

    def setUp(self):
        self.lexer = PyLexer()
        self.lexer.build()

    def tokenize_to_list(self, text):
        return [(token.type, token.value) for token in self.lexer.tokenize(text)]

    def test_simple(self):
        tokens = self.tokenize_to_list(r"AAA")
        self.assertListEqual([("PLAINTEXT", "AAA")], tokens)

        tokens = self.tokenize_to_list(r"%{}")
        self.assertListEqual([("PERC_LBRACE", "%{"), ("RBRACE", "}")], tokens)

        tokens = self.tokenize_to_list(r"\%{\}")
        self.assertListEqual([("PLAINTEXT", "%{"), ("PLAINTEXT", "}")], tokens)

        tokens = self.tokenize_to_list(r"\a")
        self.assertListEqual([("PLAINTEXT", "a")], tokens)

        tokens = self.tokenize_to_list(r"\\")
        self.assertListEqual([("PLAINTEXT", '\\')], tokens)

    def test_complex(self):
        tokens = self.tokenize_to_list("AAA${hehe}}")
        self.assertListEqual([("PLAINTEXT", "AAA"), ("DOL_LBRACE", "${"),
                          ("PLAINTEXT", "hehe"), ("RBRACE", "}"), ("PLAINTEXT", "}")], tokens)

        tokens = self.tokenize_to_list("%{\}aaa}}")
        self.assertListEqual([("PERC_LBRACE", "%{"), ("PLAINTEXT", "}"),
                          ("PLAINTEXT", "aaa"), ("RBRACE", "}"), ("PLAINTEXT", "}")], tokens)

    def test_colon(self):
        tokens = self.tokenize_to_list(
            r"aaa:hehe%{a:b}")
        self.assertListEqual([("PLAINTEXT", r"aaa"), ("PLAINTEXT", ":"), ("PLAINTEXT", "hehe"),
          ("PERC_LBRACE", "%{"), ("PLAINTEXT", "a"), ("COLON", ":"), ("PLAINTEXT", "b"), ("RBRACE", "}")], tokens)

    def test_hardcore(self):
        tokens = self.tokenize_to_list(
            r"AAiap→óðą…œó$…ðóąœ…ðóą…óA \%{edsepksofk${entity%{hehe}} \a!!–þ≠→»þ≠ó²óþ≠<<{{{{\}\}\}\}eee\}}")
        self.assertListEqual([("PLAINTEXT", r"AAiap→óðą…œó$…ðóąœ…ðóą…óA "), ("PLAINTEXT", "%{"),
                              ("PLAINTEXT", "edsepksofk"), ("DOL_LBRACE", "${"), ("PLAINTEXT", "entity"),
                              ("PERC_LBRACE", "%{"), ("PLAINTEXT", "hehe"), ("RBRACE", "}"), ("RBRACE", "}"),
                              ("PLAINTEXT", " "), ("PLAINTEXT", "a"), ("PLAINTEXT", "!!–þ≠→»þ≠ó²óþ≠<<{{{{"),
                              ("PLAINTEXT", "}"), ("PLAINTEXT", "}"), ("PLAINTEXT", "}"), ("PLAINTEXT", "}"),
                              ("PLAINTEXT", "eee"), ("PLAINTEXT", "}"), ("PLAINTEXT", "}"), ], tokens)


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = PyParser()

    def test_simple(self):

        result = self.parser.parse("aaa")
        self.assertEqual(['aaa'], result)

        result = self.parser.parse("${aaa}")
        self.assertEqual([InnerTagField(['aaa'])], result)

        result = self.parser.parse("%{aaa}")
        self.assertEqual([VariableField('aaa')], result)

    def test_escape(self):

        result = self.parser.parse("\%{}")
        # escaped, so it should be treated as plaintext, end brace has no open, so needn't be escaped...
        self.assertEqual(['%{}'], result)

        result = self.parser.parse("\%{\}")
        # ... but it can
        self.assertEqual(['%{}'], result)

    def test_invalid(self):

        # unclosed tag, so it shouldn't be parsed
        with self.assertRaises(PyslateException):
            result = self.parser.parse("%{")

        # recursive inner tags are not allowed
        with self.assertRaises(PyslateException):
            result = self.parser.parse("${${a}}")

        with self.assertRaises(PyslateException):
            result = self.parser.parse("%{%{a}}")

    def test_complicated(self):
        result = self.parser.parse("${entity_%{item}}")
        self.assertEqual([InnerTagField(["entity_", VariableField("item")])], result)

        # placeholder name based on inner tag is not allowed
        with self.assertRaises(PyslateException):
            result = self.parser.parse("%{hehe_${aaa}}")

    def test_named_inner_tags(self):
        result = self.parser.parse("You see ${giver:char_info} give ${entity_%{item_name}#u} to ${taker:char_info}.")
        self.assertEqual(["You see ", InnerTagField(["char_info"], tag_id="giver"), " give ",
                          InnerTagField(["entity_", VariableField("item_name"), "#u"]), " to ",
                          InnerTagField(["char_info"], tag_id="taker"), "."], result)

    def test_variadic(self):
        result = self.parser.parse("Kupił%{gen:m?em|f?am} kosiarkę.")

        self.assertEqual(["Kupił", SwitchField({"m": "em", "f": "am"}, "m", tag_id="gen"), " kosiarkę."], result)

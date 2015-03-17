import string
from ply import lex, yacc

class PyLexer:

    tokens = (
        'DOL_LBRACE',
        'PERC_LBRACE',
        'COLON',
        'PLAINTEXT',
        'RBRACE',
        'PIPE',
        'QUESTION',
    )

    def t_DOL_LBRACE(self, t):
        r'\${'
        self.nesting_depth += 1
        return t

    def t_PERC_LBRACE(self, t):
        r'%{'
        self.nesting_depth += 1
        return t

    def t_COLON(self, t):
        r':'
        if not self.nesting_depth:
            t.type = "PLAINTEXT"
        return t

    def t_PIPE(self, t):
        r'\|'
        if not self.nesting_depth:
            t.type = "PLAINTEXT"
        return t

    def t_QUESTION(self, t):
        r'\?'
        if not self.nesting_depth:
            t.type = "PLAINTEXT"
        return t

    t_PLAINTEXT = r'([^\$%{}\\:|?]|[^\$%}\\:|?]{|[\$%][^{}\\:|?])+'

    def t_RBRACE(self, t):
        r'}'
        if not self.nesting_depth:
            t.type = "PLAINTEXT"
        else:
            self.nesting_depth -= 1
        return t

    def t_ESCAPED(self, t):
        r'\\\${|\\\%{|\\.'
        t.type = "PLAINTEXT"
        t.value = t.value[1:]
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def __init__(self):
        self.lexer = None
        self.nesting_depth = 0

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def input(self, data, *args, **kwargs):
        return self.lexer.input(data, *args, **kwargs)

    def token(self):
        return self.lexer.token()

    def tokenize(self, data):
        self.input(data)
        return list(self.lexer)



class PyParser:

    def p_expression(self, p):
        """expression : plaintext expression
                      | variants expression
                      | inner_tag expression
                      | pholder_tag expression
                      | empty"""
        p[0] = []
        if len(p) == 3:
            p[0] += [p[1]] + p[2]
        return p[0]

    def p_pholder_tag(self, p):
        """pholder_tag : PERC_LBRACE plaintext RBRACE"""
        p[0] = VariableField(p[2])

    def p_variants_tag(self, p):
        """pholder_tag : PERC_LBRACE variants RBRACE
                       | PERC_LBRACE plaintext COLON variants RBRACE """
        if len(p) == 6:
            p[0] = SwitchField(p[4][0], p[4][1], tag_id=p[2])
        else:
            p[0] = SwitchField(p[2][0], p[2][1])

    def p_variants_variant_next(self, p):
        """variants : variant PIPE variants
                    | variant"""
        variants_dict = p[1][0]
        if len(p) == 4:
            variants_dict.update(p[3][0])
        p[0] = (variants_dict, p[1][1])  # tuple with dict and its first key

    def p_variants_variant_last(self, p):
        """variant : plaintext QUESTION plaintext"""
        variants_dict = {p[1]: p[3]}
        p[0] = (variants_dict, p[1])  # tuple with dict and its first key

    def p_variants_variant_part_next(self, p):
        """variant : plaintext QUESTION"""
        variants_dict = {p[1]: ""}
        p[0] = (variants_dict, p[1])  # tuple with dict and its first key

    def p_inner_tag(self, p):
        """inner_tag : DOL_LBRACE inner_tag_name RBRACE
                     | DOL_LBRACE plaintext COLON inner_tag_name RBRACE"""
        if len(p) == 6:
            p[0] = InnerTagField(p[4], tag_id=p[2])
        else:
            p[0] = InnerTagField(p[2])

    def p_inner_tag_name(self, p):
        """inner_tag_name : plaintext inner_tag_cont
                          | pholder_tag inner_tag_cont"""
        p[0] = [p[1]] + p[2]

    def p_inner_tag_cont(self, p):
        """inner_tag_cont : plaintext inner_tag_cont
                          | pholder_tag inner_tag_cont
                          | empty"""
        p[0] = []
        if len(p) == 3:
            p[0] += [p[1]] + p[2]

    def p_plaintext(self, p):
        """plaintext : PLAINTEXT plaintext
                     | PLAINTEXT"""

        p[0] = p[1]
        if len(p) == 3:
            p[0] += p[2]

    def p_empty(self, p):
        """empty : """
        p[0] = None

    def p_error(self, p):
        raise PyslateException(self.data)

    def __init__(self):
        self.tokens = PyLexer.tokens
        self.data = None
        self.lexer = PyLexer()
        self.lexer.build()
        self.parser = yacc.yacc(module=self, debug=1)

    def parse(self, data, **kwargs):
        self.data = data
        return self.parser.parse(data, lexer=self.lexer, **kwargs)


class InnerTagField:
    def __init__(self, contents, tag_id=None):
        self.contents = contents
        self.tag_id = tag_id
        
    def __eq__(self, other):
        return self.contents == other.contents and self.tag_id == other.tag_id

    def __repr__(self):
        return "inner tag (" + str(self.contents) + ", " + str(self.tag_id) + ")"


class VariableField:
    def __init__(self, contents):
        self.contents = contents

    def __eq__(self, other):
        return self.contents == other.contents

    def __repr__(self):
        return "placeholder(" + str(self.contents) + ")"


class SwitchField:
    def __init__(self, cases, first_key, tag_id=None):
        self.first_key = first_key
        self.cases = cases
        self.tag_id = tag_id

    def __eq__(self, other):
        return self.cases == other.cases and self.first_key == other.first_key

    def __repr__(self):
        return "variants(" + str(self.cases) + ", " + self.first_key + ")"


class PyslateException(Exception):
    def __init__(self, tag):
        self.tag = tag

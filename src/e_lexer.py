"""lexer module"""

import ply.lex as lex
import sys
import common

reserved = {
    'if': 'TKIF',
    'else': 'TKELSE',
    'while': 'TKWHILE',
    'return': 'TKRETURN',
    'int': 'TKINT',
    'real': 'TKREAL'
}

tokens = [
    'ID',
    'NUMBER',
    'NEQ',
    'GEQ',
    'LEQ',
    'AND',
    'OR',
    'ASSIGN',
] + list(reserved.values())

literals = "()[]{},;+-*/<>="


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_NUMBER = r'[0-9]+(\.[0-9]*)?'

t_NEQ = r'!='
t_LEQ = r'<='
t_GEQ = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_ASSIGN = r':='


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'


def t_eolcomment(t):
    r'//.*\n'
    t.lexer.lineno += 1


def t_comment(t):
    r'/\*([^*]|\**[^*/])*\*/'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    # pylint: disable=missing-docstring
    print("Illegal input '%s' at (%d:%d)" % (t.value[:4], t.lexer.lineno,
                                             find_column(t.lexer.lexdata, t)))
    sys.exit(1)


def find_column(inputstr, token):
    """Compute column.
     inputstr is the input text string
     token is a token instance"""
    last_cr = inputstr.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

lexer = lex.lex(outputdir=common.sourceDirectory)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        s = open(sys.argv[1]).read()
        lexer.input(s)
        while True:
            tok = lexer.token()
            print(tok)
            if not tok:
                break

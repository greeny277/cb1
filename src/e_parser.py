"""parser module"""
import ply.yacc as yacc
from e_lexer import tokens
import ast
import sys
import e_lexer
import common
from common import InternalError

# IF YOU CHANGE THE GRAMMAR:
# consider setting debug=1 in the
# yacc.yacc and parser.parse invocations below for debugging output.

# The parser generator is called PLY,
# please refer to the internet for documentation.

def p_program(p):
    '''program : program vardecl ';'
               | program funcdecl
               | vardecl ';'
               | funcdecl '''
    if len(p) == 2:
        p[0] = ast.Program().addloc(p.lineno(1))
        p[0].addfunc(p[1])
    elif len(p) == 3 and not isinstance(p[1], ast.Program):
        p[0] = ast.Program().addloc(p.lineno(1))
        p[0].addvar(p[1])
    elif len(p) == 3 and isinstance(p[1], ast.Program):
        p[0] = p[1]
        p[0].addfunc(p[2])
    elif len(p) == 4:
        p[0] = p[1]
        p[0].addvar(p[2])


def p_arraydecllist(p):
    '''arraydecl : '[' arith_expr ']' arraydecl
                 | '[' arith_expr ']' '''
    if len(p) == 5:
        p[0] = [p[2]] + p[4]
    else:
        p[0] = [p[2]]


def p_vardecl(p):
    '''vardecl : type identifier
               | type arraydecl identifier'''
    if len(p) == 4:
        # declaration of an array
        p[0] = ast.VarDecl(p[1], p[3]).addloc(p.lineno(1))
        p[0].addArray(p[2])
    else:
        p[0] = ast.VarDecl(p[1], p[2]).addloc(p.lineno(1))


def p_funcdecl(p):
    '''funcdecl : type identifier '(' parList ')' block
                | type identifier '('         ')' block'''
    if len(p) == 7:
        p[0] = ast.Function(p[1], p[2], p[4], p[6]).addloc(p.lineno(1))

    else:
        p[0] = ast.Function(p[1], p[2], [], p[5]).addloc(p.lineno(1))


def p_identifier(p):
    '''identifier : ID'''
    p[0] = ast.Identifier(p[1]).addloc(p.lineno(1))


def p_type_primitive(p):
    '''type : TKREAL
           | TKINT
           | TKBOOL
           | type arraydecl '''
    if p[1] == "int":
        p[0] = common.Type.getIntType()
    elif p[1] == "real":
        p[0] = common.Type.getRealType()
    elif p[1] == "bool":
        p[0] = common.Type.getBoolType()
    else:
        raise common.InputError("invalid Type: " + repr(p[1]))
    if len(p) == 3:
        p[0] = p[0].getArrayType(p[2])



def p_parList_single(p):
    '''parList : vardecl'''
    p[0] = [p[1]]


def p_parList_mult(p):
    '''parList : parList ',' vardecl '''
    p[0] = p[1] + [p[3]]


def p_block(p):
    '''block : '{' vardecllist stmtlist '}'
             | '{' vardecllist '}'
             | '{' stmtlist '}'
             | '{' '}' '''
    p[0] = ast.Block().addloc(p.lineno(1))
    if len(p) == 4:
        for y in p[2]:
            if isinstance(y, ast.VarDecl):
                p[0].addVardecl(y)
            else:
                p[0].addStatement(y)
    elif len(p) == 5:
        for vd in p[2]:
            p[0].addVardecl(vd)
        for st in p[3]:
            p[0].addStatement(st)


def p_vardecllist(p):
    '''vardecllist : vardecl ';'
                   | vardecllist vardecl ';' '''
    if len(p) == 4:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_stmtlist(p):
    '''stmtlist : stmt
                | stmtlist stmt '''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_stmt(p):
    '''stmt : ifstmt
            | assgnstmt
            | whilestmt
            | returnstmt
            | block '''
    p[0] = p[1]


def p_ifstmt(p):
    '''ifstmt : TKIF '(' cond_expr ')' block TKELSE block
              | TKIF '(' cond_expr ')' block '''
    if len(p) == 8:
        p[0] = ast.IfStmt(p[3], p[5], p[7]).addloc(p.lineno(1))
    else:
        p[0] = ast.IfStmt(p[3], p[5], ast.Block()).addloc(p.lineno(1))


def p_returnstmt(p):
    '''returnstmt : TKRETURN arith_expr ';' '''
    p[0] = ast.ReturnStmt(p[2]).addloc(p.lineno(1))


def p_whilestmt(p):
    '''whilestmt : TKWHILE '(' cond_expr ')' block'''
    p[0] = ast.WhileStmt(p[3], p[5]).addloc(p.lineno(1))


def p_assgnstmt(p):
    '''assgnstmt : lvalue ASSIGN arith_expr ';' '''
    p[0] = ast.AssignStmt(p[1], p[3]).addloc(p.lineno(1))


def p_lvalue(p):
    '''lvalue : identifier
              | lvalue '[' arith_expr ']' '''
    if len(p) == 2:
        p[0] = ast.LValue(p[1]).addloc(p.lineno(1))
    else:
        p[0] = p[1]
        p[0].addArrayDeref(p[3])


def p_cond_expr(p):
    '''cond_expr : cond_expr AND ao_expr
                 | cond_expr OR ao_expr
                 | ao_expr '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ast.CondExpr(p[1], ast.Operator(p[2]), p[3]).addloc(p.lineno(1))


def p_ao_expr_br(p):
    '''ao_expr : '(' cond_expr ')' '''
    p[0] = p[2]


def p_ao_expr_comp(p):
    '''ao_expr : arith_expr '='   arith_expr
               | arith_expr NEQ   arith_expr
               | arith_expr '>'   arith_expr
               | arith_expr '<'   arith_expr
               | arith_expr GEQ arith_expr
               | arith_expr LEQ arith_expr '''
    p[0] = ast.CondExpr(p[1], ast.Operator(p[2]), p[3]).addloc(p.lineno(1))


def p_arith_expr(p):
    '''arith_expr : arith_expr '+' term
                  | arith_expr '-' term
                  | term '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ast.ArithExpr(p[1],
                             ast.Operator(p[2]),
                             p[3]).addloc(p.lineno(1))


def p_term(p):
    '''term : term '*' factor
            | term '/' factor
            | factor '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ast.ArithExpr(p[1],
                             ast.Operator(p[2]),
                             p[3]).addloc(p.lineno(1))


def p_factor_funcall(p):
    '''factor : identifier '(' arg_list ')'
              | identifier '(' ')' '''
    if len(p) == 4:
        p[0] = ast.FuncCall(p[1], []).addloc(p.lineno(1))
    else:
        p[0] = ast.FuncCall(p[1], p[3]).addloc(p.lineno(1))


def p_factor_nofuncall(p):
    '''factor : '(' arith_expr ')'
              | constant
              | lvalue '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]


def p_constant(p):
    '''constant : NUMBER'''
    if '.' in p[1]:
        p[0] = ast.FloatLiteral(p[1]).addloc(p.lineno(1))
    else:
        p[0] = ast.IntLiteral(p[1]).addloc(p.lineno(1))


def p_arg_list(p):
    '''arg_list : arg_list ',' arith_expr
                | arith_expr '''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_error(p):
    print("syntax error at line " + str(p.lineno) + " with: " + p.type
          + " " + str(type(p)) + " " + repr(p))
    sys.exit(1)


parser = yacc.yacc(debug=0, start='program', outputdir=common.sourceDirectory)


def doParsing(filename):
    s = open(filename).read()
    l = e_lexer.lexer
    l.input(s)
    return parser.parse(lexer=l, debug=0, tracking=True)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        x = doParsing(sys.argv[1])
        print(x)

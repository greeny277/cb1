"""module for creating a Dot-File based on the AST"""

from ast import \
    Program, \
    VarDecl, \
    Function, \
    Identifier, \
    Type, \
    Block, \
    AssignStmt, \
    IfStmt, \
    WhileStmt, \
    ReturnStmt, \
    LValue, \
    IntLiteral, \
    FloatLiteral, \
    Operator, \
    ArithExpr, \
    FuncCall, \
    CondExpr
from dumpAST import dump

from common import InternalError

""" Global id for dot file
"""
_dot_id = 0


def dump(node, fd):
    global _dot_id
    my_id = _dot_id
    _dot_id = _dot_id + 1
    if isinstance(node, Program):
        fd.write("digraph AST {\n")
        fd.write(str(my_id) + "[label=\"program\"]\n")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
        fd.write("}")
    elif isinstance(node, VarDecl):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=VarDecl]")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
    elif isinstance(node, Identifier):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=")
        fd.write(node.name)
        fd.write("]")

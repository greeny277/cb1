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
        fd.write(str(my_id) + "[label=\"VarDecl\"]\n")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
    elif isinstance(node, Identifier):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"")
        fd.write(node.name)
        fd.write("\"]\n")
    elif isinstance(node, Type):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"")
        fd.write(node.desc() + "\"]\n")
    elif isinstance(node, Block):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"BLOCK\"]\n")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
    elif isinstance(node, AssignStmt):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\":=\"]\n")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
    elif isinstance(node, IfStmt):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"IF\"]\n")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
    elif isinstance(node, WhileStmt):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"WHILE\"]\n")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
    elif isinstance(node, WhileStmt):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"RETURN\"]\n")
        fd.write(str(my_id) + " -> ")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
    elif isinstance(node, LValue):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"LValue\"]\n")
        fd.write(str(my_id) + " -> ")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
    elif isinstance(node, IntLiteral) \
            or isinstance(node, FloatLiteral) \
            or isinstance(node, Operator):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"")
        fd.write(node.name)
        fd.write("\"]\n")
    elif isinstance(node, ArithExpr):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"ArithExpr\"]\n")
        fd.write(str(my_id) + " -> ")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
    elif isinstance(node, CondExpr):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"CondExpr\"]\n")
        fd.write(str(my_id) + " -> ")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)
    elif isinstance(node, FuncCall):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + "[label=\"FuncCall\"]\n")
        fd.write(str(my_id) + " -> ")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dump(c, fd)


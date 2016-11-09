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

from common import InternalError
import dumpAST

""" Global id for dot file
"""
_dot_id = 0


def dumpDot(node, fd):
    global _dot_id
    print("GLOBAL DOTID: " + str(_dot_id))
    my_id = _dot_id
    _dot_id = _dot_id + 1
    print("My DOTID: " + str(my_id))
    if isinstance(node, Program):
        fd.write("digraph AST {\n")
        fd.write(str(my_id) + " [label=\"program\"];\n")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dumpDot(c, fd)
        fd.write("}")
    elif isinstance(node, Function):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"FuncDecl: ")
        dumpAST.dump(node.type, fd)
        fd.write(" id: ")
        dumpAST.dump(node.name, fd)
        fd.write("\"];\n")
        fd.write(str(my_id) + " -> ")
        parlist_id = _dot_id
        _dot_id = _dot_id + 1
        fd.write(str(parlist_id) + ";\n")
        fd.write(str(parlist_id) + " [label=\"ParList\"];\n")
        for c in node.arglist:
            fd.write(str(parlist_id) + " -> ")
            dumpDot(c, fd)
        fd.write(str(my_id) + " -> ")
        dumpDot(node.block, fd)
    elif isinstance(node, VarDecl):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"VarDecl: ")
        dumpAST.dump(node.type, fd)
        for x in node.array:
            fd.write("[]")
        fd.write(" id: ")
        dumpAST.dump(node.name, fd)
        fd.write("\"];\n")
    elif isinstance(node, Identifier):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"")
        fd.write(node.name)
        fd.write("\"];\n")
    elif isinstance(node, Type):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"")
        fd.write(node.desc() + "\"]\n")
    elif isinstance(node, Block):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"BLOCK\"];\n")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dumpDot(c, fd)
    elif isinstance(node, AssignStmt):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\":=\"];\n")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dumpDot(c, fd)
    elif isinstance(node, IfStmt):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"IF-COND\"];\n")
        " Create THEN path "
        then_id = _dot_id
        _dot_id = _dot_id + 1
        fd.write(str(my_id) + " -> " + str(then_id) + ";\n")
        fd.write(str(then_id) + " [label=\"THEN\"];\n")
        " Create COND path "
        cond_id = _dot_id
        _dot_id = _dot_id + 1
        fd.write(str(my_id) + " -> " + str(cond_id) + ";\n")
        fd.write(str(cond_id) + " [label=\"COND\"];\n")
        " Create ELSE path "
        else_id = _dot_id
        _dot_id = _dot_id + 1
        fd.write(str(my_id) + " -> " + str(else_id) + ";\n")
        fd.write(str(else_id) + " [label=\"ELSE\"];\n")


        fd.write(str(then_id) + " -> ")
        dumpDot(node.trueblock, fd)
        fd.write(str(cond_id) + " -> ")
        dumpDot(node.cond, fd)
        fd.write(str(else_id) + " -> ")
        dumpDot(node.falseblock, fd)

    elif isinstance(node, WhileStmt):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"WHILE\"];\n")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dumpDot(c, fd)
    elif isinstance(node, ReturnStmt):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"RETURN\"];\n")
        fd.write(str(my_id) + " -> ")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dumpDot(c, fd)
    elif isinstance(node, LValue):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"LValue\"];\n")
        fd.write(str(my_id) + " -> ")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dumpDot(c, fd)
    elif isinstance(node, IntLiteral) \
            or isinstance(node, FloatLiteral) \
            or isinstance(node, Operator):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"")
        fd.write(node.val)
        fd.write("\"];\n")
    elif isinstance(node, ArithExpr):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"ArithExpr\"];\n")
        fd.write(str(my_id) + " -> ")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dumpDot(c, fd)
    elif isinstance(node, CondExpr):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"CondExpr\"];\n")
        fd.write(str(my_id) + " -> ")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dumpDot(c, fd)
    elif isinstance(node, FuncCall):
        fd.write(str(my_id) + ";\n")
        fd.write(str(my_id) + " [label=\"FuncCall\"];\n")
        fd.write(str(my_id) + " -> ")
        for c in node.children():
            fd.write(str(my_id) + " -> ")
            dumpDot(c, fd)
    else:
        print("-----------MISSING IMPLEMENTATION-------------")
        print(type(node))
        print("-----------------------------------------------")


"""module for dumping an AST"""

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


def dump(node, fd, indentlvl=0, varDeclSpecialCase=False):
    """Method to dump the AST starting at node to fd"""
    # pylint: disable=too-many-branches,too-many-statements
    if isinstance(node, Program):
        for c in node.children():
            dump(c, fd)
    elif isinstance(node, VarDecl):
        if not varDeclSpecialCase:
            fd.write(" " * indentlvl)
        dump(node.type, fd)
        fd.write(" ")
        dump(node.name, fd)
        if not varDeclSpecialCase:
            fd.write(";\n")
    elif isinstance(node, Function):
        dump(node.type, fd)
        fd.write(" ")
        dump(node.name, fd)
        fd.write(" (")
        sep = ""
        for a in node.arglist:
            fd.write(sep)
            dump(a, fd, varDeclSpecialCase=True)
            sep = ", "
        fd.write(")\n")
        dump(node.block, fd)
    elif isinstance(node, Identifier):
        fd.write(node.name)
    elif isinstance(node, Type):
        fd.write(node.desc())
    elif isinstance(node, Block):
        fd.write(" " * indentlvl + "{\n")
        for l in node.children():
            dump(l, fd, indentlvl + 2)
        fd.write(" " * indentlvl + "}\n")
    elif isinstance(node, AssignStmt):
        fd.write(" " * indentlvl)
        dump(node.lvalue, fd)
        fd.write(" := ")
        dump(node.expr, fd)
        fd.write(";\n")
    elif isinstance(node, IfStmt):
        fd.write(" " * indentlvl + "if(")
        dump(node.cond, fd)
        fd.write("){\n")
        for l in node.trueblock.children():
            dump(l, fd, indentlvl + 2)
        fd.write(" " * indentlvl + "} else {\n")
        for l in node.falseblock.children():
            dump(l, fd, indentlvl + 2)
        fd.write(" " * indentlvl + "}\n")
    elif isinstance(node, ReturnStmt):
        fd.write(" " * indentlvl + "return ")
        dump(node.expr, fd)
        fd.write(";\n")
    elif isinstance(node, WhileStmt):
        fd.write(" " * indentlvl + "while(")
        dump(node.cond, fd)
        fd.write(")\n")
        dump(node.block, fd)
        fd.write(" " * indentlvl + "\n")
    elif isinstance(node, LValue):
        dump(node.name, fd)
        for l in node.arrayDeref:
            fd.write("[")
            dump(l, fd)
            fd.write("]")
    elif isinstance(node, IntLiteral) \
            or isinstance(node, FloatLiteral) \
            or isinstance(node, Operator):
        fd.write(node.val)
    elif isinstance(node, ArithExpr):
        fd.write("(")
        dump(node.left, fd)
        fd.write(" ")
        dump(node.op, fd)
        fd.write(" ")
        dump(node.right, fd)
        fd.write(")")
    elif isinstance(node, CondExpr):
        fd.write("(")
        dump(node.left, fd)
        fd.write(" ")
        dump(node.op, fd)
        fd.write(" ")
        dump(node.right, fd)
        fd.write(")")
    elif isinstance(node, FuncCall):
        dump(node.func_name, fd)
        fd.write("(")
        for x in node.par_list:
            dump(x, fd)
        fd.write(")")
    else:
        raise InternalError("unimplemented ast node type")

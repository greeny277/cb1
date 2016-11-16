"""module for traversing the AST and assemble the symbol table"""
import symboltable
import sys
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

from common import Variable, InputError
s = symboltable.SymbolTable()

def traverse(node):
    """traverse the AST, creating entries for the symbol table and check if vars
    are declared etc.
    """

    if isinstance(node, Function):
        s.enterScope()
        var = Variable(node.name, node.type)
        try:
            s.insertVariable(var)
        except InputError as err:
            print(format(err))
        for a in node.arglist:
            argListVar = Variable(a.name, a.type)
            try:
                s.insertVariable(argListVar)
            except InputError as err:
                print(format(err))
                sys.exit(1)
        traverse(node.block)
        s.leaveScope()
    elif isinstance(node, Block):
        s.enterScope()
        for l in node.children():
            traverse(l)
        s.leaveScope()
    elif isinstance(node, VarDecl):
        var = Variable(node.name, node.type)
        try:
            s.insertVariable(var)
        except InputError as err:
            print(format(err))
            sys.exit(1)
    elif isinstance(node, Identifier):
        """ check if identifier exists in symboltable"""
        try:
            node.decl = s.queryVarName(node.name)
        except InputError as err:
            print(format(err))
            sys.exit(1)
    else:
        for c in node.children():
            traverse(c)

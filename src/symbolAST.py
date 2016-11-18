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
lib = None


def setLibAST(libAST):
    global lib
    lib = libAST


def initLib(node):
    if isinstance(node, Function):
        var = Variable(node.name.name, node.type)
        try:
            s.insertVariable(var)
        except InputError as err:
            print(format(err) + ": " + node.name.name)
    else:
        for c in node.children():
            initLib(c)


def traverse(node):
    """traverse the AST, creating entries for the symbol table and check if vars
    are declared etc.
    """
    if isinstance(node, Program):
        initLib(lib)
    if isinstance(node, Function):
        var = Variable(node.name.name, node.type)
        try:
            s.insertVariable(var)
        except InputError as err:
            print(format(err) + ": " + node.name.name)
        
        s.enterScope()
        for a in node.arglist:
            argListVar = Variable(a.name.name, a.type)
            try:
                s.insertVariable(argListVar)
            except InputError as err:
                print(format(err) + ": " + node.name.name)
                sys.exit(1)

        traverse(node.block)
        s.leaveScope()


    elif isinstance(node, Block):
        s.enterScope()
        for l in node.children():
            traverse(l)
        s.leaveScope()
    elif isinstance(node, VarDecl):
        var = Variable(node.name.name, node.type)
        try:
            s.insertVariable(var)
        except InputError as err:
            print(format(err) + ": " + node.name.name)
            sys.exit(1)
    elif isinstance(node, Identifier):
        """ check if identifier exists in symboltable"""
        try:
            node.decl = s.queryVarName(node.name)
        except InputError as err:
            print(format(err) + ": " + node.name)
            sys.exit(1)
    else:
        for c in node.children():
            traverse(c)

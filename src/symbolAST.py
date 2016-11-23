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
        var = Variable(node.name.name, node.type, node)
        try:
            s.insertVariable(var)
        except InputError as err:
            print(format(err) + ": " + node.name.name)
            sys.exit(1)
    else:
        for c in node.children():
            initLib(c)


def traverse(node):
    """traverse the AST, creating entries for the symbol table and check if vars
    are declared etc.
    """
    if isinstance(node, Program):
        """print("DEBUG: Start init lib")"""
        initLib(lib)
        """print("DEBUG: End init lib")"""
    if isinstance(node, Function):
        var = Variable(node.name.name, node.type, node)
        try:
            print("DEBUG FUNCTION: " + "Name: " + node.name.name + " Type:" + str(node.type))
            s.insertVariable(var)
        except InputError as err:
            print(format(err) + ": " + node.name.name)
            sys.exit(1)

        s.enterScope()
        for a in node.arglist:
            print("DEBUG ARGLIST: " + "Name: " + a.name.name + " Type:" + str(a.type))
            argListVar = Variable(a.name.name, a.type, a)
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
        print("DEBUG: ADD VarDecl: Name:" + node.name.name + " Type" + str(node.type))
        var = Variable(node.name.name, node.type, node)
        try:
            s.insertVariable(var)
        except InputError as err:
            print(format(err) + ": " + node.name.name)
            sys.exit(1)
    elif isinstance(node, Identifier):
        """ check if identifier exists in symboltable"""
        try:
            var = s.queryVarName(node.name)
            node.setDecl(var.getDecl())
            print("DEBUG SetDecl: Node name: " + node.name + "; Decl Type " + str(type(var.getDecl())))
        except InputError as err:
            print(format(err) + ": " + node.name)
            sys.exit(1)
    else:
        for c in node.children():
            traverse(c)

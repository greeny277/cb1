""" This module implements a symboltable. """
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


class SymbolTable(object):
    """ Symboltable class """
    def __init__(self):
        self.hashTable = {}
        self.lastEntry = None
        self.currentDepth = 0

    def enterScope(self):
        """
        Enter new Scope. Mark last added Variable.
        """
        self.currentDepth = self.currentDepth + 1
        if self.lastEntry is not None:
            self.lastEntry.setTos(True)

    def leaveScope(self):
        """ Leave current Scope. Traverse last added Variables
        backwards until a Variable which is declared as TopOfStack
        will be found.
        """
        if self.lastEntry is None:
            return

        while self.lastEntry.isTos() is False:
            del self.hashTable[self.lastEntry.name]
            self.lastEntry = self.lastEntry.getPreviuos()

        self.lastEntry.setTos(False)
        self.currentDepth = self.currentDepth - 1

    def insertVariable(self, variable):
        """
        Members:
        variable: Variable adding to hashtable

        Returns nothing, but adds when possible a
        new variable to the internal hashtable
        """
        checkVar = self.hashTable.get(variable.name)
        if checkVar is None:
            self.hashTable[variable.name] = [variable]
        elif checkVar[0].getDepth() != self.currentDepth:
            self.hashTable[variable.name] = [variable]+checkVar
        else:
            raise InputError("Double variable declaration in same scope")
        variable.setDepth(self.currentDepth)
        variable.setPreviuos(self.lastEntry)
        self.lastEntry = variable

    def queryVarName(self, name):
        """
        Members:
        name: Identifier of a variable or function

        Return:
        Variable object declared in most inner scope or None
        """
        checkVar = self.hashTable.get(name)
        if checkVar is None:
            raise InputError("Variable not declared")
        else:
            return checkVar[0]

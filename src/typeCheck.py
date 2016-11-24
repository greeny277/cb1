"""module for type checking the ast"""
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
    CondExpr, \
    ToReal, \
    ToInt

from common import Variable, InputError

'''Save in this variable return type of current function'''
functionReturnType = None

def typeChecking(node):
    """traverse the AST and add conversion nodes"""

    print("DEBUG: Type of Node:" + str(type(node)))
    if isinstance(node, Identifier):
        ident = node.getDecl()
        print("DEBUG: Identifier instance: " + str(type(ident)))
        if isinstance(ident, VarDecl):
            return ident.type
        elif isinstance(ident, Function):
            ''' TODO:this call might be wrong'''
            return typeChecking(ident)


    elif isinstance(node, FuncCall):
        ''' Get corresponding Function Object'''
        funcObj = node.func_name.getDecl()
        if len(funcObj.arglist) != len(node.par_list):
            '''Number of parameter for function call does not match'''
            raise InputError("Number of parameter does not match at " + str(node.func_name))
        for x in node.par_list:
            print("DUMMY BEGIN")
            typeChecking(x)
            print("DUMMY END")
        return funcObj.getType()
    elif isinstance(node, ArithExpr):
        leftType = typeChecking(node.left)
        rightType = typeChecking(node.right)

        if leftType != rightType:
            if leftType == Type.getIntType():
                '''Add ToReal node on left side'''
                node.left = ToReal(node.left)
            else:
                '''Add ToReal node on right side'''
                node.right = ToReal(node.right)
    elif isinstance(node, AssignStmt):
        leftType = typeChecking(node.lvalue)
        rightType = typeChecking(node.expr)
        if leftType != rightType:
            if leftType == Type.getIntType():
                '''Add ToInt cast on right side'''
                node.expr = ToInt(node.expr)
            else:
                '''Add ToReal cast on right side'''
                node.expr = ToReal(node.expr)
    elif isinstance(node, Function):
        global functionReturnType
        functionReturnType = node.getType()
        ''' check the arguments of the function, e.g. array forbidden '''
        for a in node.arglist:
            if len(a.array) != 0:
                raise InputError("Argument is an array: " + str(node.name))
        typeChecking(node.block)
    elif isinstance(node, VarDecl):
        accessors = node.getArray()
        for a in accessors:
            if Type.getIntType() != typeChecking(a):
                raise InputError("Invalid array access in VarDecl: " + str(node.name))
    elif isinstance(node, LValue):
        accessors = node.getArrayDeref()
        decl = node.name.getDecl()
        if isinstance(decl, VarDecl):
            if len(node.getArrayDeref()) != len(decl.getArray()):
                raise InputError("Invalid array access in LValue: " + str(node.name))

        for a in accessors:
            if Type.getRealType() == typeChecking(a):
                raise InputError("Invalid array access in LValue: " + str(node.name))
            else:
                typeChecking(a)

        if isinstance(node.name.getDecl(), Function):
                raise InputError("The function misses its arguments: " + str(node.name))

        return decl.type

    elif isinstance(node, Program):
        for c in node.children():
            typeChecking(c)
    elif isinstance(node, ReturnStmt):
        returnType = typeChecking(node.expr)

        if returnType != functionReturnType:
            if returnType == Type.getIntType():
                node.expr = ToReal(node.expr)
            else:
                node.expr = ToInt(node.expr)
    elif isinstance(node, IntLiteral):
        return Type.getIntType()
    elif isinstance(node, FloatLiteral):
        return Type.getRealType()
    else:
        for x in node.children():
            typeChecking(x)

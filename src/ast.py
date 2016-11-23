"""module for ast nodes"""

from common import InternalError, Type


class AstNode(object):
    """ abstract base class for all ast nodes. Contains line number info,
    if set by the parser.

    Members:
    line: line number. -1 if not set by parser.
    """

    def __init__(self):
        self.line = -1

    def children(self):
        """This method returns an iterator over all child nodes of
        this ast node"""
        # pylint: disable=no-self-use
        raise InternalError("unimplemented")

    def desc(self):
        """short description of node; intended for internal use"""
        # pylint: disable=no-self-use
        return ""

    def __str__(self, indentlvl=0):
        """toString method..."""
        retstring = " " * indentlvl + str(self.__class__.__name__)
        retstring += " " + self.desc() + (" @%d" % (self.line))
        for child in self.children():
            if isinstance(child, AstNode):
                retstring += "\n" + child.__str__(indentlvl + 2)
            else:
                retstring += "\n" + " " * (indentlvl + 2) + repr(child)
        return retstring

    def addloc(self, line):
        """method to add line information to this node"""
        self.line = line
        return self

    def typecheck(self, totest, expectedtype):
        """typechecks this ast node"""
        # pylint: disable=no-self-use
        if not isinstance(totest, expectedtype):
            raise InternalError("expected " + repr(expectedtype)
                                + " but got " + repr(type(totest)))


class Program(AstNode):
    """ast node representing a whole program

    Members:
    vars: global variables
    funcs: functions
    """
    def __init__(self):
        super(Program, self).__init__()
        self.vars = []
        self.funcs = []

    def addvar(self, var):
        """adds a variable declaration to the program"""
        self.vars.append(var)

    def addfunc(self, func):
        """adds a function definition to the program"""
        self.funcs.append(func)

    def children(self):
        return self.vars + self.funcs

_DeclID = 0


class VarDecl(AstNode):
    """Declaration of one variable.

    Members:
    name: name of variable
    type: type of variable
    id: unique id of this declaration
    array: list of arith expressions defining index"""

    def __init__(self, _type, name):
        # pylint: disable=global-statement
        super(VarDecl, self).__init__()
        global _DeclID
        self.type = _type
        self.name = name
        self.id = _DeclID
        _DeclID = _DeclID + 1
        self.array = []

    def children(self):
        yield self.type
        for x in self.array:
            yield x
        yield self.name

    def desc(self):
        return str(self.id)

    def getType(self):
        """returns type of this variable declaration"""
        return self.type
    
    def addArray(self, arr):
        """ adds the array index expressions to the list """
        self.array = arr

    def getArray(self):
        """ Return array index expressiopns"""
        return self.array


class Function(AstNode):
    """Function Definition.

    Members:
    type: return type
    name: identifier with function name
    arglist: list of VarDecl with function arguments
    block: body of function
    id: unique id of this function"""
    def __init__(self, _type, name, arglist, block):
        super(Function, self).__init__()
        # pylint: disable=global-statement
        global _DeclID
        self.type = _type
        self.name = name
        self.arglist = arglist
        self.block = block
        self.id = _DeclID
        _DeclID = _DeclID + 1

    def children(self):
        yield self.type
        yield self.name
        for arg in self.arglist:
            yield arg
        yield self.block

    def desc(self):
        return str(self.id)

    def getType(self):
        """returns the return type of this function"""
        return self.type


class Identifier(AstNode):
    """identifier

    Members:
    name: name of identifier
    decl: VarDecl or Function that this identifier refers to"""
    def __init__(self, name):
        super(Identifier, self).__init__()
        self.name = name
        self.decl = None

    def children(self):
        return []

    def setDecl(self, decl):
        """sets reference to the declaration this
        identifier refers to"""
        self.decl = decl

    def getDecl(self):
        """Return decl object"""
        return self.decl

    def desc(self):
        if self.decl is not None:
            return self.name + " " + self.decl.desc()
        return self.name


class Statement(AstNode):
    """parent class for ast nodes representing statements"""
    pass


class Block(Statement):
    """class representing a block

    Members:
    statements: list of statements in this block
    vardecls: list of variables local to this block"""
    def __init__(self):
        super(Block, self).__init__()
        self.statements = []
        self.vardecls = []

    def addStatement(self, st):
        """adds statement to this block"""
        self.statements.append(st)

    def addVardecl(self, vd):
        """adds vardecl to this block"""
        self.vardecls.append(vd)

    def children(self):
        return self.vardecls + self.statements


class AssignStmt(Statement):
    """class representing an assignment

    Members:
    lvalue: target of this assignment
    expr: source value of this assignment
    type_left: type of lvalue
    type_right: type of expr """
    def __init__(self, lvalue, expr, type_left=None, type_right=None):
        super(AssignStmt, self).__init__()
        self.lvalue = lvalue
        self.expr = expr
        self.type_left = type_left
        self.type_right = type_right

    def children(self):
        yield self.lvalue
        yield self.expr

    def set_left_type(self, t):
        self.type_left = t

    def get_left_type(self, t):
        return self.type_left

    def set_right_type(self, t):
        self.type_right = t

    def get_right_type(self, t):
        return self.type_right


class IfStmt(Statement):
    """class representing an if statement

    Members:
    cond: condition
    trueblock: block to be executed if cond evaluates to true
    falseblock: block to be executed if cond evaluates to false"""
    def __init__(self, cond, trueblock, falseblock):
        super(IfStmt, self).__init__()
        self.cond = cond
        self.trueblock = trueblock
        self.falseblock = falseblock

    def children(self):
        yield self.cond
        yield self.trueblock
        yield self.falseblock


class ReturnStmt(Statement):
    """class representing a return statement

    Members:
    expr: expression to return"""
    def __init__(self, expr):
        super(ReturnStmt, self).__init__()
        self.expr = expr

    def children(self):
        yield self.expr


class WhileStmt(Statement):
    """class representing a while statement

    Members:
    cond: condition
    block: body of the statement"""
    def __init__(self, cond, block):
        super(WhileStmt, self).__init__()
        self.cond = cond
        self.block = block

    def children(self):
        yield self.cond
        yield self.block


class Expression(AstNode):
    """base class representing expressions

    Members:
    type: type of whatever this expression evaluates to"""
    def __init__(self):
        super(Expression, self).__init__()
        self.type = None

    def setType(self, _type):
        "sets the type of this expression"
        self.type = _type

    def getType(self):
        "returns the type of this expression"
        return self.type


class LValue(Expression):
    """class representing an lvalue, i.e. an expression that can be assigned to

    Members:
    name: Identifier
    arrayDeref: possibly empty list of array access expressions"""
    def __init__(self, name):
        super(LValue, self).__init__()
        self.name = name
        self.arrayDeref = []

    def children(self):
        yield self.name
        for x in self.arrayDeref:
            yield x

    def addArrayDeref(self, ad):
        """adds an array access to this lvalue"""
        self.arrayDeref.append(ad)
    def getArrayDeref(self):
        """return array access list"""
        return self.arrayDeref

    def desc(self):
        return self.name.desc()


class Literal(Expression):
    """base class for literals.

    Members:
    val: value of this literal
    type: type of this literal"""
    def __init__(self, val, _type):
        super(Literal, self).__init__()
        self.val = val
        self.type = _type

    def children(self):
        return []

    def desc(self):
        return str(self.val)


class IntLiteral(Literal):
    """class representing integer literals"""
    def __init__(self, val):
        super(IntLiteral, self).__init__(val, Type.getIntType())


class FloatLiteral(Literal):
    """class representing float literals"""
    def __init__(self, val):
        super(FloatLiteral, self).__init__(val, Type.getRealType())


class FuncCall(Expression):
    """Declaration of a function call
    Members:
    func_name: identifier of the function
    par_list: parameter list of the function
    """
    def __init__(self, func_name, par_list):
        super(FuncCall, self).__init__()
        self.func_name = func_name
        self.par_list = par_list

    def children(self):
        yield self.func_name
        for x in self.par_list:
            yield x


class ArithExpr(Expression):
    """class representing an arithmetic expression

    Members:
    left: left subexpression
    op: infix operator
    right: right subexpression"""
    def __init__(self, left, op, right):
        super(ArithExpr, self).__init__()
        self.typecheck(left, Expression)
        self.typecheck(right, Expression)
        self.left = left
        self.op = op
        self.right = right

    def children(self):
        yield self.left
        yield self.op
        yield self.right

    def desc(self):
        if self.getType() is not None:
            return self.getType().desc()
        return ""


class CondExpr(Expression):
    """class representing a conditional expression

    Members:
    left: left subexpression
    op: infix operator
    right: right subexpression"""
    def __init__(self, left, op, right):
        super(CondExpr, self).__init__()
        self.left = left
        self.op = op
        self.right = right

    def children(self):
        yield self.left
        yield self.op
        yield self.right


class Operator(AstNode):
    """class representing an operator

    Members:
    val: string describing this operator"""
    def __init__(self, val):
        super(Operator, self).__init__()
        self.val = val

    def children(self):
        return []

    def desc(self):
        return self.val


class ToReal(Expression):
    """class for representing conversion from int to real
    Members:
    successor: ast node to be converted, can be: subexpression or identifier
    type: return type of this conversion
    """
    def __init__(self, successor):
        super(ToReal, self).__init__()
        self.type = Type.getRealType()
        self.successor = successor

    def children(self):
        yield self.successor


class ToInt(Expression):
    """class for representing conversion from real to int
    Members:
    successor: ast node to be converted, can be: subexpression or identifier
    type: return type of this conversion
    """
    def __init__(self, successor):
        super(ToInt, self).__init__()
        self.type = Type.getIntType()
        self.successor = successor

    def children(self):
        yield self.successor

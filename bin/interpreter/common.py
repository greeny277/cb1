"""this module contains common stuff, p.ex.
exception classes for use in the e python compiler."""

import os
import sys
from io import StringIO


class Error(Exception):
    """Base class for all errors occurring in the e python compiler.
    Please use this if you want to raise an Exception"""
    pass


class InternalError(Error):
    """base class for any errors caused by bugs or missing
    features in your own code"""
    def __init__(self, msg, line=-1):
        super(InternalError, self).__init__(msg + (" @%d" % (line)))


class InputError(Error):
    """base class for any errors caused by wrong input programs
    (grammar errors, type errors, use of undeclared variables, etc)"""
    def __init__(self, msg, line):
        super(InputError, self).__init__(msg + (" @%d" % (line)))


def warning(msg, line=-1):
    """print a warning message to stderr"""
    if line != -1:
        sys.stderr.write("%s @%d\n" % (msg, line))
    else:
        sys.stderr.write("%s\n" % (msg))


class Type(object):
    """class for representing a Type in E """
    def __init__(self, typename):
        """constructor. do not call explicitly, please use
        getIntType, getRealType and getArrayType instead."""
        self._name = typename
        self._dims = []
        self._sdl = None

    _real = None
    _int = None
    _bool = None

    @classmethod
    def getIntType(cls):
        """returns a Type object describing an integer type"""
        return cls._int

    @classmethod
    def getRealType(cls):
        """returns a type object describing a real type"""
        return cls._real

    @classmethod
    def getBoolType(cls):
        """returns a type object describing a boolean type"""
        return cls._bool

    def getArrayType(self, dimExpr):
        """returns a type object, describing an array of some base type.
        needs an expression as argument, describing the size of the array."""
        # pylint: disable=protected-access
        r = Type(self._name)
        r._dims = list(self._dims)
        r._dims.append(dimExpr)
        return r

    def getSimpleDimList(self):
        """returns a list of integers describing the size of the
        dimensions of the array type"""
        # print(str(self._dims))
        if self._sdl is None:
            self._sdl = []
            for ex in self._dims:
                # pylint: disable=cyclic-import
                if isinstance(ex, str):
                    self._sdl.append(int(ex))
                else:
                    import e_ast
                    if not isinstance(ex, e_ast.IntLiteral):
                        raise InternalError("need int literal")
                    self._sdl.append(int(ex.val))
        return self._sdl

    def desc(self):
        """returns a string describing this type"""
        x = self._name
        if len(self._dims) == 0:
            return x
        # pylint: disable=cyclic-import
        import dumpAST
        buf = StringIO()
        for dd in self._dims:
            buf.write("[")
            dumpAST.dump(dd, buf)
            buf.write("]")
        return x + buf.getvalue()

    def children(self):
        """dummy implementation, see astnode.children"""
        for expr in self._dims:
            yield expr

    def isPrimitive(self):
        """returns true iff this type is a primitive type"""
        return len(self._dims) == 0

    def isArray(self):
        """returns true iff this type is an array type"""
        return len(self._dims) != 0

    def getBaseType(self):
        """if self is array type, returns base type, else returns self"""
        if self.isPrimitive():
            return self
        if self._name == "real":
            return Type._real
        if self._name == "int":
            return Type._int
        if self._name == "bool":
            return Type._bool

    def __eq__(self, other):
        # pylint: disable=protected-access
        if not isinstance(other, Type):
            return False
        if self._name != other._name:
            return False
        if self.getSimpleDimList() != other.getSimpleDimList():
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def getArrayDims(self):
        """returns the list of array dimension expressions"""
        return self._dims

    def getSizeInBytes(self):
        """returns the size an element of this type needs"""
        rv = 8
        for dim in self.getSimpleDimList():
            rv *= dim
        return rv


# pylint: disable=protected-access
Type._real = Type("real")
Type._int = Type("int")
Type._bool = Type("bool")
# pylint: enable=protected-access


class Variable(object):
    """class representing a variable, parameter or function in the AST.

    Members:
    name: name of this variable
    type: type of this variable
    decl: location where this variable is declared"""
    def __init__(self, name, declaration):
        self.name = name
        self.type = None
        self.decl = declaration
        self.offset = 0
        self.serID = -1

    def getName(self):
        """returns the variable's name"""
        return self.name

    def getType(self):
        """returns the variable's type"""
        if self.type is None:
            self.type = self.decl.type
        return self.type

    def setType(self, _type):
        """sets the variable's type"""
        self.type = _type

    def getDecl(self):
        """returns the location where this variable was declared"""
        return self.decl

    def desc(self):
        """returns a short description of this variable"""
        return str(self.decl.id) + " " + self.getType().desc()

    def isFunction(self):
        """returns true iff this is a Function"""
        # pylint: disable=cyclic-import
        import ast
        return isinstance(self.decl, ast.Function)

    def parameterTypes(self):
        """returns a list with the parameter types of this function"""
        xx = []
        if not self.isFunction():
            return xx
        for arg in self.decl.arglist:
            xx.append(arg.type)
        return xx

# global variable to access the command line arguments, set in main.py
runtimeArgs = None

# global variable to access the directory of the compiler's source code
sourceDirectory = os.path.dirname(os.path.realpath(__file__))


# def typecheck(var, expectedType):
#     """check type of var against expectedType
#     and raise InternalError on mismatch"""
#     if not isinstance(var, expectedType):
#         raise InternalError("expected type %s, got %s"
#                             % (expectedType, type(var)), -1)

def typecheck(func, expectedType = None):
    if expectedType is not None:
        return
    tocheck = [func.__annotations__.get(func.__code__.co_varnames[i], None)
               for i in range(func.__code__.co_argcount)]
    for x in tocheck:
        if x is not None:
            assert isinstance(x, type)    
    def wrap(*args, **kwargs):
        for neededtype, actualarg in zip(tocheck, args):
            if neededtype is not None:
                if not isinstance(actualarg, neededtype):
                    raise InternalError("expected type %s, got %s"
                                        % (neededtype, type(actualarg)), -1)
        return func(*args, **kwargs)

    return wrap

# (c) Jakob Krainz, 2015
def MultipleDispatch(func):
    """multiple dispatch in python with function annotations. Usage:

    @MultipleDispatch
    def test2(a):
        print("test2 default: " + str(a))
    @test2.dispatch
    def test2(a: str):
        print("test2 str: " + a)
    @test2.dispatch
    def test2(a: int):
        print("test2 int: " + str(a))
    test2(None) # will print "test2 default: None"
    test2("a")  # will print "test2 str: a"
    test2(12)   # will print "test2 int: 12"

    CAVEAT: The alternatives will be tried in reversed order
    (i.e. last one added will be tried first). The first alternative
    whose types fit will be called.

    Annotations may be instances of <class 'type'>. in this case
    "isinstance(actual argument, annotation)" will be checked.

    Alternatively, they may be callable. In this case,
    "annotation(actual argument)" will be checked.
    """

    def _hlp(func):
        """given a function, returns a tuple, consisting of:
           - a list of the function's arguments' annotations, or None if no annotation is there
           - the function itself"""
        tocheck = [func.__annotations__.get(func.__code__.co_varnames[i], None)
                   for i in range(func.__code__.co_argcount)]
        return (tocheck, func)

    # torun: list of tuples as returned by _hlp
    torun = [_hlp(func)]

    def _wrapper(*args, **kwargs):
        """traverses torun, checks if the arguments in *args 
           match the type annotation given there, if so -> "func" is called,
           else: Exception"""
        for tocheck, runnable in reversed(torun):
            fits = True
            for i in range(len(tocheck)):
                if tocheck[i] is not None:
                    # print(">>> %d %r %r" % (i, tocheck[i], args[i]))
                    # first, check if the annotation is a type
                    if isinstance(tocheck[i], type):
                        # if it is, check if the actual argument is an
                        # instance of that type
                        if isinstance(args[i], tocheck[i]):
                            continue
                    # second, check if the annotation is callable
                    elif callable(tocheck[i]):
                        # if it is, check if it returns true on the
                        # actual argument
                        if tocheck[i](args[i]):
                            continue
                    # if neither is true, the actual argument does not
                    # fit this annotation, thus we need to check the
                    # next function
                    fits = False
                    break
            if fits:
                return runnable(*args, **kwargs)
        raise Exception("no fitting function found")

    def _dispatch(nextfunc):
        """dispatch(f) shall add f to "torun" """
        torun.append(_hlp(nextfunc))
        return _wrapper

    # this turns _wrapper.dispatch into a new function annotation,
    # which will add the annotated function to _wrapper's torun list
    _wrapper.dispatch = _dispatch
    return _wrapper
   
if __name__ == '__main__':
    @MultipleDispatch
    def test(X, b, c, **kwargs):
        print("test Nothing Nothing")
    
    @test.dispatch
    def test(X: int, b: str, c):
        print("test int str")
    
    @test.dispatch
    def test(X: str, b: str, c):
        print("test str str")
    test("2", "3", 0)
    test(2, "3", -1)
    test(2, 3, -1)

    @MultipleDispatch
    def test2(a):
        print("test2 default : " + str(a))

    @test2.dispatch
    def test2(a: str):
        print("test2 str : " + a)

    @test2.dispatch
    def test2(a: int):
        print("test2 int : " + str(a))

    test2(None)
    test2("a")
    test2(12)
    
    @MultipleDispatch
    def test3(a: str):
        print("test3 str : " + a)

    @test3.dispatch
    def test3(a: int):
        print("test3 int : " + str(a))

    test3("b")
    test3(14)
    try:
        test3(None)
    except Exception as e:
        print("caught exception: " + repr(e))

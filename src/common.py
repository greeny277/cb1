"""this module contains common stuff, p.ex.
exception classes for use in the e python compiler."""

import os


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


class Type(object):
    """class for representing a Type in E """
    def __init__(self, typename, _dims=[]):
        """constructor. do not call explicitly, please use
        getIntType, getRealType and getArrayType instead."""
        self._name = typename
        self._dims = _dims.copy()
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
        return Type(self._name, self._dims + [dimExpr])

    def getSimpleDimList(self):
        """returns a list of integers describing the size of the
        dimensions of the array type"""
        if self._sdl is None:
            self._sdl = []
            for ex in self._dims:
                import ast
                if not isinstance(ex, ast.IntLiteral):
                    raise InternalError("need int literal")
                self._sdl.append(int(ex.val))
        return self._sdl

    def desc(self):
        """returns a string describing this type"""
        x = self._name
        if len(self._dims) == 0:
            return x
        from io import StringIO
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


Type._real = Type("real")
Type._int = Type("int")
Type._bool = Type("bool")

# global variable to access the command line arguments, set in main.py
runtimeArgs = None

# global variable to access the directory of the compiler's source code
sourceDirectory = os.path.dirname(os.path.realpath(__file__))


def typecheck(var, expectedType):
    """check type of var against expectedType
    and raise InternalError on mismatch"""
    if not isinstance(var, expectedType):
        raise InternalError("expected type %s, got %s"
                            % (expectedType, type(var)), -1)

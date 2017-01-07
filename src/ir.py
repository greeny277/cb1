"""These classes make up the intermediate representation of the e language."""
from collections import OrderedDict
from common import typecheck
import common


class Operand(object):
    """operand for ir instruction"""
    def __init__(self, value):
        typecheck(value, OperandValue)
        self.__val = value

    def __str__(self):
        return str(self.val)

    @property
    def type(self):
        "type of operand"
        return self.val.getType()

    @property
    def val(self):
        "variable, register or constant, whatever this operand represents"
        return self.__val

    # pylint: disable=missing-docstring
    @val.setter
    def val(self, val):
        typecheck(val, OperandValue)
        self.__val = val
        return self.__val

    def __eq__(self, other):
        try:
            return self.val == other.val and self.type == other.type
        except AttributeError:
            return False


class OperandValue(object):
    """base class for the value of an operand"""
    # pylint: disable=too-few-public-methods
    _operanduidsrc = 0

    def __init__(self, _type):
        self.__type = _type
        typecheck(_type, common.Type)
        self.uid = OperandValue._operanduidsrc
        OperandValue._operanduidsrc += 1

    @property
    def type(self):
        "type of operand"
        return self.__type


class ConstValue(OperandValue):
    """constant literal operand value for ir instruction"""
    def __init__(self, value, _type):
        super(ConstValue, self).__init__(_type)
        self.__val = value

    def __str__(self):
        return str(self.val)

    @property
    def val(self):
        "const value of this operand"
        return self.__val

    def __eq__(self, other):
        try:
            return self.val == other.val and self.type == other.type
        except AttributeError:
            return False


class Register(OperandValue):
    """class to represent registers in the IR"""
    def __init__(self, name, _type):
        super(Register, self).__init__(_type)
        self.__name = name

    @property
    def name(self):
        """this register's name"""
        return self.__name

    def prettyprint(self, _file):
        """ prettyprinter for dumping this register to _file"""
        xstr = "reg " + self.name + " " + self.type.desc()
        _file.write(xstr + "\n")

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Reg:" + self.name

    def __eq__(self, other):
        try:
            return self.name == other.name and self.type == other.type
        except AttributeError:
            return False

    def __hash__(self):
        return hash(self.name)


class VirtualRegister(Register):
    """class to represent virtual registers"""
    # pylint: disable=too-few-public-methods
    pass


class HardwareRegister(Register):
    """class to represent hardware registers"""
    # pylint: disable=too-few-public-methods
    pass


class IRProgram(object):
    """wrapper class for ir of whole program"""
    def __init__(self):
        self.__variables = []
        self.__functions = []
        self._nextlabelid = 0
        self._nextvregid = 0
        self._used_names = set()

    def prettyprint(self, _file):
        """ prettyprinter for dumping the program to _file"""
        for var in self.variables:
            var.prettyprint(_file)
        for fun in self.functions:
            fun.prettyprint(_file)

    def consCheck(self):
        """consistency check method"""
        names = set()
        for var in self.variables:
            assert isinstance(var, IRVariable)
            assert var.name not in names
            names.add(var.name)
        for fun in self.functions:
            assert isinstance(fun, IRFunction)
            fun.consCheck(self)
            assert fun.name not in names
            names.add(fun.name)

    def genLabel(self):
        """generate new, unused label"""
        self._nextlabelid += 1
        return CLABEL(self._nextlabelid)


    def getFreeVirtReg(self, _type):
        """creates new, globally unique virtual register and returns it"""
        typecheck(_type, common.Type)
        while True:
            name = "%R"+str(self._nextvregid)
            self._nextvregid += 1
            if not name in self._used_names:
                break
        reg = VirtualRegister(name, _type)
        self._used_names.add(name)
        return reg

    def getUnusedName(self, name):
        ext = ""
        extid = 0
        while name + ext in self._used_names:
            extid += 1
            ext = '$' + str(extid)
        self._used_names.add(name+ext)
        return name+ext

    def getIRVar(self, name, _type, isGlobal=False):
        """generates new, unused variable with specified type.
        The name of the new var starts with name, and is globally unique"""
        name = self.getUnusedName(name)
        irv = IRVariable(name, _type, isGlobal)
        return irv

    @property
    def variables(self):
        "global variables"
        return self.__variables

    @property
    def functions(self):
        "global functions"
        return self.__functions


class IRVariable(OperandValue):
    """IR Variable or array, global or function-local

    The name of the variable should be unique, globally or inside the
    Variable's function.
    """
    # pylint: disable=too-few-public-methods
    def __init__(self, name, _type, isGlobal):
        super(IRVariable, self).__init__(_type)
        self.__name = name
        self.__isGlobal = isGlobal

    def prettyprint(self, _file):
        """ prettyprinter for dumping this variable to _file"""
        xstr = "var " + self.name + " " + self.type.desc()
        _file.write(xstr + "\n")

    def __str__(self):
        return self.name

    def __repr__(self):
        return "IRvar:" + self.name

    @property
    def name(self):
        "this variable's name"
        return self.__name

    @property
    def isGlobal(self):
        "true iff this variable is global"
        return self.__isGlobal


# pylint: disable=too-many-instance-attributes
class IRFunction(object):
    """ IR Function

    Members:
    name: Name of this function
    params: Parameters of this function
    vars: local variables of this function
    virtRegs: virtual registers used by this function
    """
    def __init__(self, name, irprogram):
        self.name = irprogram.getUnusedName(name)
        self.params = OrderedDict()
        self.vars = OrderedDict()
        self.virtRegs = OrderedDict()
        self._firstInstr = None
        self._lastInstr = None
        self.isPredefined = False
        self._nextvregid = 0

    def prettyprint(self, _file):
        """ prettyprinter for dumping this function to _file"""
        _file.write("Function " + self.name + "\n")
        _file.write(" local vars\n")
        for val in self.vars.values():
            _file.write("  ")
            val.prettyprint(_file)
        _file.write(" params\n")
        for val in self.params.values():
            _file.write("  ")
            val.prettyprint(_file)
        _file.write(" registers\n")
        for val in self.virtRegs.values():
            _file.write("  ")
            val.prettyprint(_file)
        _file.write(" code\n")
        for instr in self.instrs():
            if isinstance(instr, CLABEL):
                indent = "  "
            else:
                indent = "    "
            _file.write(indent + str(instr) + "\n")

    def addInstr(self, instr):
        """appends instruction to function"""
        typecheck(instr, ICode)
        if self._firstInstr is None:
            self._firstInstr = self._lastInstr = instr
            instr.function = self
        else:
            self._lastInstr.insertAfter(instr)

    def insertInstr(self, instr):
        """prepends instruction to function"""
        typecheck(instr, ICode)
        if self._firstInstr is None:
            self._firstInstr = self._lastInstr = instr
            instr.function = self
        else:
            self._firstInstr.insertBefore(instr)

    def addVar(self, var):
        """adds local variable to function"""
        typecheck(var, IRVariable)
        # assert not var.name in self.virtRegs
        self.vars[var.name] = var

    def addParam(self, var):
        """adds parameter to function"""
        typecheck(var, IRVariable)
        self.params[var.name] = var

    def instrsreversed(self):
        """returns a reverse-iterator over the instructions of this function"""
        x = self._lastInstr
        while x is not None:
            # now we can remove x and continue iterating :)
            x_prev = x.prev
            yield x
            x = x_prev

    def instrs(self):
        """returns an iterator over the instructions of this function"""
        x = self._firstInstr
        while x is not None:
            # now we can remove x and continue iterating :)
            x_next = x.next
            yield x
            x = x_next

    def consCheck(self):
        """consistency check helper method"""
        if self._firstInstr is None or self._lastInstr is None:
            assert self._firstInstr is None
            assert self._lastInstr is None
            return
        assert self._firstInstr.prev is None
        assert self._lastInstr.next is None
        fast = self._firstInstr
        slow = self._firstInstr
        odd = False
        while True:
            assert isinstance(fast, ICode)
            assert fast.function is self
            if fast.next is None:
                assert fast is self._lastInstr
                break
            assert fast.next.prev is fast
            fast = fast.next
            if odd:
                slow = slow.next
            odd = not odd
            assert slow is not fast


class ICode(object):
    """base class for IR instructions"""
    def __init__(self):
        self.__next = None
        self.__prev = None
        self.function = None

    def __str__(self):
        return self.__class__.__name__

    def insertBefore(self, otherinstr):
        """inserts otherinstr before this instruction
        in this instruction's function"""
        # pylint: disable=protected-access
        if self.__prev is None:
            self.__prev = otherinstr
            otherinstr.__next = self
            otherinstr.function = self.function
            self.function._firstInstr = otherinstr
        else:
            otherinstr.__next = self
            otherinstr.function = self.function
            otherinstr.__prev = self.__prev
            self.__prev = otherinstr
            otherinstr.__prev.__next = otherinstr

    def insertAfter(self, otherinstr):
        """inserts otherinstr after this instruction
        in this instruction's function"""
        # pylint: disable=protected-access
        if self.__next is None:
            self.__next = otherinstr
            otherinstr.__prev = self
            otherinstr.function = self.function
            self.function._lastInstr = otherinstr
        else:
            otherinstr.__prev = self
            otherinstr.function = self.function
            otherinstr.__next = self.__next
            self.__next = otherinstr
            otherinstr.__next.__prev = otherinstr

    def remove(self):
        """removes this instruction from this instruction's function"""
        # pylint: disable=protected-access
        if self.__next is None and self.__prev is None:
            self.function._firstInstr = self.function._lastInstr = None
        elif self.__next is None:
            self.function._lastInstr = self.__prev
            self.__prev.__next = None
        elif self.__prev is None:
            self.function._firstInstr = self.__next
            self.__next.__prev = None
        else:
            self.__prev.__next = self.__next
            self.__next.__prev = self.__prev
        self.__prev = self.__next = self.function = None

    @property
    def prev(self):
        """the preceding instruction"""
        return self.__prev

    @property
    def next(self):
        """the next instruction"""
        return self.__next

    def getOperandsRead(self):
        """returns a list of operands read in this instruction"""
        # pylint: disable=no-self-use
        return []

    def getOperandsWritten(self):
        """returns a list of operands written in this instruction"""
        # pylint: disable=no-self-use
        return []


class CTarget(ICode):
    """base class for IR instructions with one target operand

    Members:
    target: target operand of this instruction"""
    def __init__(self, target):
        super(CTarget, self).__init__()
        typecheck(target, OperandValue)
        self.__target = Operand(target)

    def getOperandsWritten(self):
        return [self.target]

    @property
    def target(self):
        "target operand of this instruction"
        return self.__target


class CSingle(ICode):
    """base class for IR instructions with one source operand

    Members:
    source: source operand of this instruction"""
    def __init__(self, source):
        super(CSingle, self).__init__()
        typecheck(source, OperandValue)
        self.__source = Operand(source)

    def __str__(self):
        return self.__class__.__name__ + " " \
            + str(self.source)

    def getOperandsRead(self):
        return [self.source]

    @property
    def source(self):
        "source operand of this instruction"
        return self.__source


class CBinary(CTarget):
    """base class for IR instructions with two source operands
    and one target operand

    Members:
    left: left source operand of this instruction
    right: right source operand of this instruction"""
    def __init__(self, target, left, right):
        super(CBinary, self).__init__(target)
        typecheck(left, OperandValue)
        typecheck(right, OperandValue)
        self.__left = Operand(left)
        self.__right = Operand(right)

    def __str__(self):
        if isinstance(self, CMUL):
            op = ' * '
        elif isinstance(self, CADD):
            op = ' + '
        elif isinstance(self, CSUB):
            op = ' - '
        elif isinstance(self, CDIV):
            op = ' / '

        return str(self.target) + " = " \
            + str(self.left) + op + str(self.right)

    def getOperandsRead(self):
        return [self.left, self.right]

    @property
    def left(self):
        "left source operand of this instruction"
        return self.__left

    @property
    def right(self):
        "right source operand of this instruction"
        return self.__right


class CUnary(CTarget):
    """base class for IR instructions with one source operand
    and one target operand

    Members:
    src: source operand of this instruction"""
    def __init__(self, target, source):
        super(CUnary, self).__init__(target)
        typecheck(source, OperandValue)
        self.__source = Operand(source)

    def __str__(self):
        return self.__class__.__name__ + " " \
            + str(self.target) + " " + str(self.source)

    def getOperandsRead(self):
        return [self.source]

    @property
    def source(self):
        "source operand of this instruction"
        return self.__source


# label and jump instructions
class CLABEL(ICode):
    """pseudo instruction representing target of jump instructions"""
    def __init__(self, myid):
        super(CLABEL, self).__init__()
        self.id = myid

    def __str__(self):
        return "L" + str(self.id)+":"


class CBranch(ICode):
    """base class for all jump instructions"""
    def __init__(self, label):
        super(CBranch, self).__init__()
        typecheck(label, CLABEL)
        self.__label = label

    @property
    def label(self):
        "label this instruction (maybe) jumps to"
        return self.__label

    def __str__(self):
        return self.__class__.__name__ \
            + " L" + str(self.label.id)

    # pylint: disable=missing-docstring
    @label.setter
    def label(self, label):
        typecheck(label, CLABEL)
        self.__label = label


class CCondBranch(CBranch):
    """base class for conditional jump instructions"""
    def __init__(self, label, left, right):
        super(CCondBranch, self).__init__(label)
        typecheck(left, OperandValue)
        typecheck(right, OperandValue)
        self.__left = Operand(left)
        self.__right = Operand(right)

    def __str__(self):
        return self.__class__.__name__ \
            + " " + str(self.left) + ", " + str(self.right) \
            + ", L" + str(self.label.id)

    def getOperandsRead(self):
        return [self.left, self.right]

    @property
    def left(self):
        "left source operand of this instruction"
        return self.__left

    @property
    def right(self):
        "right source operand of this instruction"
        return self.__right


class CBEQ(CCondBranch):
    """jump if equal instruction"""
    def __init__(self, label, left, right):
        super(CBEQ, self).__init__(label, left, right)


class CBGE(CCondBranch):
    """jump if greater or equal instruction"""
    def __init__(self, label, left, right):
        super(CBGE, self).__init__(label, left, right)


class CBGT(CCondBranch):
    """jump if greater instruction"""
    def __init__(self, label, left, right):
        super(CBGT, self).__init__(label, left, right)


class CBLE(CCondBranch):
    """jump if less or equal instruction"""
    def __init__(self, label, left, right):
        super(CBLE, self).__init__(label, left, right)


class CBLT(CCondBranch):
    """jump if less instruction"""
    def __init__(self, label, left, right):
        super(CBLT, self).__init__(label, left, right)


class CBNE(CCondBranch):
    """jump if not equal instruction"""
    def __init__(self, label, left, right):
        super(CBNE, self).__init__(label, left, right)


class CBRA(CBranch):
    """unconditiona jump instruction"""
    def __init__(self, label):
        super(CBRA, self).__init__(label)


class CPOP(CTarget):
    """instruction to save single argument to stack
    only used by the backend, to save/restore caller/callee save registers"""
    pass


# function call instructions
class CPUSH(CSingle):
    """instruction to push single argument to function call or
    (by the backend) to save/restore caller/callee save registers to stack"""
    pass


class CRET(CSingle):
    """instruction to return from function"""
    pass


class CCALL(CTarget):
    """instruction to call function and store return value"""
    def __init__(self, target, name):
        super(CCALL, self).__init__(target)
        self.__name = name

    def __str__(self):
        return str(self.target) + " = " \
            + "CALL [" \
            + str(self.name) + "]"

    @property
    def name(self):
        "name of target function"
        return self.__name

# arithmetic instructions

class CADD(CBinary):
    """instruction to add two operands"""
    pass


class CDIV(CBinary):
    """instruction to divide two operands"""
    pass


class CMUL(CBinary):
    """instruction to multiply two operands"""
    pass


class CSUB(CBinary):
    """instruction to subtract two operands"""
    pass


class CI2R(CUnary):
    """instruction to cast int to real"""
    pass


class CR2I(CUnary):
    """instruction to cast real to int"""
    pass

# MOV instructions


class CASSGN(CUnary):
    """instruction to assign value to variable"""
    def __str__(self):
        return str(self.target) + " = " + str(self.source)


class CLOAD(CTarget):
    """instruction to load value from array"""
    def __init__(self, target, base, offset):
        super(CLOAD, self).__init__(target)
        typecheck(base, OperandValue)
        typecheck(offset, OperandValue)
        self.__base = Operand(base)
        self.__offset = Operand(offset)

    def __str__(self):
        return str(self.target) + " = " \
            + str(self.base) + "[" \
            + str(self.offset) + "]"

    def getOperandsRead(self):
        return [self.base, self.offset]

    @property
    def base(self):
        "base address of array"
        return self.__base

    @property
    def offset(self):
        "offset inside array"
        return self.__offset


class CSTORE(ICode):
    """instruction to store value to array"""
    def __init__(self, target, offset, value):
        super(CSTORE, self).__init__()
        typecheck(target, OperandValue)
        typecheck(offset, OperandValue)
        typecheck(value, OperandValue)
        self.__target = Operand(target)
        self.__offset = Operand(offset)
        self.__value = Operand(value)

    def __str__(self):
        return str(self.target) + "[" + str(self.offset) \
            + "] = " + str(self.value)

    def getOperandsRead(self):
        return [self.value, self.offset]

    def getOperandsWritten(self):
        return [self.target]

    @property
    def target(self):
        "base address of array"
        return self.__target

    @property
    def offset(self):
        "offset inside array"
        return self.__offset

    @property
    def value(self):
        "value to store in array"
        return self.__value

"""interpreter"""
from ir import *
from common import Type
import sys

def execICode(self, context):
    raise Exception("not implemented")

def monkeyPatch():
    ICode.exec = execICode
    CBRA  .exec = execCBRA  
    CBEQ  .exec = execCBEQ  
    CBGE  .exec = execCBGE  
    CBGT  .exec = execCBGT  
    CBLE  .exec = execCBLE  
    CBLT  .exec = execCBLT  
    CBNE  .exec = execCBNE  
    CLABEL.exec = execCLABEL
    CSTORE.exec = execCSTORE
    CPUSH .exec = execCPUSH 
    CRET  .exec = execCRET  
    CADD  .exec = execCADD  
    CDIV  .exec = execCDIV  
    CMUL  .exec = execCMUL  
    CSUB  .exec = execCSUB  
    CCALL .exec = execCCALL 
    CLOAD .exec = execCLOAD 
    CPHI  .exec = execCPHI  
    CPOP  .exec = execCPOP  
    CI2R  .exec = execCI2R  
    CR2I  .exec = execCR2I  
    CASSGN.exec = execCASSGN


def _hlp(s, c, func):
    if func(c.get(s.left), c.get(s.right)):
        return s.label
    else:
        return s.next
    
def execCBEQ(s, c): return _hlp(s, c, lambda a, b: a == b)
def execCBNE(s, c): return _hlp(s, c, lambda a, b: a != b)
def execCBGT(s, c): return _hlp(s, c, lambda a, b: a >  b)
def execCBLT(s, c): return _hlp(s, c, lambda a, b: a <  b)
def execCBGE(s, c): return _hlp(s, c, lambda a, b: a >= b)
def execCBLE(s, c): return _hlp(s, c, lambda a, b: a <= b)

def execCBRA  (self, context):
    return self.label

def execCLABEL(self, context):
    return self.next

def execCADD  (self, context):
    context.setVar(self.target, (context.get(self.left) + context.get(self.right)))
    return self.next

def execCDIV  (self, context):
    context.setVar(self.target, (context.get(self.left) // context.get(self.right)))
    return self.next

def execCMUL  (self, context):
    context.setVar(self.target, (context.get(self.left) * context.get(self.right)))
    return self.next

def execCSUB  (self, context):
    context.setVar(self.target, (context.get(self.left) - context.get(self.right)))
    return self.next

def execCASSGN(self, context):
    context.setVar(self.target, context.get(self.source))
    return self.next

def execCSTORE(self, context):
    context.setArr(self.target, context.get(self.offset), context.get(self.value))
    return self.next

def execCLOAD (self, context):
    context.setVar(self.target, context.getArr(self.base, context.get(self.offset)))
    return self.next

def execCPUSH (self, context):
    context.setFuncArg(context.get(self.source))
    return self.next

def execCRET  (self, context):
    context.exitStatus = context.get(self.source)
    return None

def execCCALL (self, context):
    ret = interp(context.lookupFunction(self.name), context)
    context.clearFuncArgs()
    context.setVar(self.target, ret)
    return self.next

def execCPHI  (self, context): raise Exception("not implemented")
def execCPOP  (self, context): raise Exception("not implemented")
def execCI2R  (self, context): raise Exception("not implemented")
def execCR2I  (self, context): raise Exception("not implemented")


def writeChar(char):
    sys.stdout.write(chr(char))
    return 1

def readChar():
    return ord(sys.stdin.read(1))

def readInt():
    x = ""
    while True:
        k = sys.stdin.read(1)
        if k in "-0123456789":
            x = x + k
            break
    while True:
        k = sys.stdin.read(1)
        if k in "0123456789":
            x = x + k
        elif x == "":
            pass
        else:
            #sys.stderr.write("read int : " + x + "\n")
            return int(x)
        
def writeInt(x):
    sys.stdout.write(str(x))
    return len(str(x))

def exit(x):
    sys.exit(x)

def time():
    import time
    millis = int(round(time.time() * 1000))
    return millis

class Context(object):
    def __init__(self, program):
        self.vars = [{}]
        self.program = program
        self.funcArgs = [[]]
        self.exitStatus = None
        for var in program.variables:
            self.addVar(var)

    def lookupFunction(self, funname):
        for func in self.program.functions:
            if func.name == funname:
                return func
        if funname == "writeChar":
            return writeChar
        elif funname == "readChar":
            return readChar
        elif funname == "writeInt":
            return writeInt
        elif funname == "readInt":
            return readInt
        elif funname == "exit":
            return exit
        elif funname == "time":
            return time
        raise Exception("function " + funname + " not found")
            
    def addVar(self, var):
        if var.type.isPrimitive():
            vv = 0
        else:
            vv = [ 0 for _ in range(var.type.getSizeInBytes()//8) ]
        self.vars[-1][var.name] = vv
            
    def enter(self, function):
        self.vars.append({})
        for var in function.vars.values():
            self.addVar(var)
        for var in function.virtRegs.values():
            self.addVar(var)
        assert len(self.getAllArgs()) == len(function.params.values())
        for idx, var in enumerate(reversed(function.params.values())):
            self.addVar(var)
            self.setVar(var, self.getFuncArg(idx))
        #print("enter", function.name,  self.funcArgs[-1])
        self.funcArgs.append([])

    def leave(self):
        self.vars.pop()
        self.funcArgs.pop()
        #print("leave", self.funcArgs[-1], file=sys.stderr)

    def setFuncArg(self, val):
        self.funcArgs[-1].append(val)

    def clearFuncArgs(self):
        self.funcArgs[-1].clear()

    def getFuncArg(self, idx):
        return self.funcArgs[-1][idx]

    def getAllArgs(self):
        return self.funcArgs[-1]
    
    def get(self, var):
        if isinstance(var, Operand):
            var = var.val
        assert isinstance(var, OperandValue)
        if isinstance(var, ConstValue):
            vv = var.val
            if var.type == Type.getIntType():
                return int(var.val)
            else:
                return float(var.val)
        name = var.name
        for idx in [-1, 0]:
            if name in self.vars[idx]:
                vv = self.vars[idx][name]
                # print("get: ", str(var), "@", idx,  " -> " + str(vv), file=sys.stderr)
                return vv
        raise Exception("variable " + repr(var) + " not found")
        
    def getArr(self, var, offset):
        if isinstance(var, Operand):
            var = var.val
        assert isinstance(var, IRVariable)
        name = var.name
        for idx in [-1, 0]:
            if name in self.vars[idx]:
                return self.vars[idx][name][offset]
        raise Exception("variable " + repr(var) + " not found")

    def setVar(self, var, val):
        if isinstance(var, Operand):
            var = var.val
        assert isinstance(var, (IRVariable, VirtualRegister))
        name = var.name
        for idx in [-1, 0]:
            if name in self.vars[idx]:
                self.vars[idx][name] = val
                return
        raise Exception("variable " + repr(var) + " not found")

    def setArr(self, var, offset, val):
        if isinstance(var, Operand):
            var = var.val
        assert isinstance(var, IRVariable)
        name = var.name
        for idx in [-1, 0]:
            if name in self.vars[idx]:
                self.vars[idx][name][offset] = val
                return
        raise Exception("variable " + repr(var) + " not found")


def interp(function, context):
    if isinstance(function, IRFunction):
        # print("entering function " + function.name, file = sys.stderr)
        context.enter(function)
        _next = function.first
        while _next:
            # print("next: "+ str(_next), file=sys.stderr)
            _next = _next.exec(context)
        context.leave()
        # print("leaving function " + function.name, file = sys.stderr)
        return context.exitStatus
    else:
        exitstatus = function(*reversed(context.getAllArgs()))
        return exitstatus

def interpret(prog):
    monkeyPatch()
    sys.setrecursionlimit(10000000)
    context = Context(prog)
    for f in prog.functions:
        if f.name == 'main':
            return interp(f, context)
    raise Exception("no main function found")

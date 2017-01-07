""" module for generating intermediate code """ 
from ir import \
        IRProgram, \
        IRFunction, \
        IRVariable, \
        ConstValue, \
        CR2I, \
        CLOAD, \
        CADD, \
        CSUB, \
        CMUL, \
        CDIV, \
        CPUSH, \
        CCALL, \
        CRET, \
        CASSGN

from ast import \
        Program, \
        VarDecl, \
        Function, \
        Block, \
        Identifier, \
        Type, \
        AssignStmt, \
        ReturnStmt, \
        LValue, \
        IntLiteral, \
        FloatLiteral, \
        Literal, \
        ArithExpr, \
        FuncCall, \
        ToReal, \
        ToInt

# TODO check default value for parameter


def irgen(node, irprogram=None, irfunction=None):
    if isinstance(node, Program):
        irprogram = IRProgram()
        for v in node.vars:  # TODO use addGlobal(?)
            irprogram.variables.append(irgen(v))

        for f in node.funcs:  # TODO use addFunc(?)
            irprogram.functions.append(irgen(f, irprogram))

        return irprogram
    elif isinstance(node, Function):
        irfunction = IRFunction(node.name.name, irprogram)
        for par in node.arglist:
            irfunction.addParam(irgen(par, irprogram, irfunction))
        irgen(node.block, irprogram, irfunction)
    elif isinstance(node, VarDecl):
        irvar = irprogram.getIRVar(node.name, node.type)
        irfunction.addVar(irvar)
    elif isinstance(node, Block):
        for x in node.children():
            irgen(x, irprogram, irfunction)
    elif isinstance(node, Identifier):
        if node.name in irfunction.vars:
            return irfunction.vars[node.name]
        elif node.name in irfunction.params:
            return irfunction.params[node.name]
        else:
            print("This should never happen o.0")
    elif isinstance(node, ToInt):
        tmp = irgen(node.successor, irprogram, irfunction)
        virtReg = irprogram.getFreeVirtReg(Type.getIntType())
        irfunction.addInstr(CR2I(virtReg, tmp))
        irfunction.virtRegs[virtReg.name] = virtReg
        return virtReg
    elif isinstance(node, ToReal):
        tmp = irgen(node.successor, irprogram, irfunction)
        virtReg = irprogram.getFreeVirtReg(Type.getRealType())
        irfunction.addInstr(CR2I(virtReg, tmp))
        irfunction.virtRegs[virtReg.name] = virtReg
        return virtReg
    elif isinstance(node, Literal):
        return ConstValue(node.val, node.type)
    elif isinstance(node, LValue):
        decl = node.name.getDecl()
        derefs = decl.getArrayDeref()
        if len(derefs) != 0:
            # is array
            offset = 0
            dims = node.name.getDecl().getArray()
            # compute index for 1-dim array storage
            for i in range(0, len(derefs)):
                    for j in range(i+1, len(dims)):
                        offset += derefs[i]*dims[j]

            offset += derefs[len(derefs)-1]
            virtReg = irprogram.getFreeVirtReg(decl.type.getBaseType())
            base = None
            if node.name.name in irfunction.vars:
                base = irfunction.vars[node.name.name]
            elif node.name.name in irfunction.params:
                base = irfunction.params[node.name.name]
            else:
                print("This should never happen o.0")
            irfunction.addInstr(CLOAD(virtReg, base, offset))
            return virtReg
        else:
            return irgen(node.name, irprogram, irfunction)

    elif isinstance(node, ArithExpr):
        # Evaluate leftern subtree
        leftReg = irgen(node.left, irprogram, irfunction)
        # Evaluate rightern subtree
        rightReg = irgen(node.right, irprogram, irfunction)

        if rightReg.type() != leftReg.type():
            print("ArithExpr: Subexpressions have different type :'(")

        destReg = irprogram.getFreeVirtReg(rightReg.type())

        if node.op.val == "+":
            irfunction.addInstr(CADD(leftReg, rightReg, destReg))
        elif node.op.val == "-":
            irfunction.addInstr(CSUB(leftReg, rightReg, destReg))
        elif node.op.val == "*":
            irfunction.addInstr(CMUL(leftReg, rightReg, destReg))
        elif node.op.val == "/":
            irfunction.addInstr(CDIV(leftReg, rightReg, destReg))
        else:
            print("ArithExpr: Another mysterious error: No valid operand")

        return destReg

    elif isinstance(node, FuncCall):
        for p in reversed(node.par_list):
            irfunction.addInstr(CPUSH(p))

        # get the return type of the func call
        returnType = node.func_name.getDecl().getType()
        destReg = irprogram.getFreeVirtualReg(returnType)
        irfunction.addInstr(CCALL(node.func_name.name, destReg))
    elif isinstance(node, ReturnStmt):
        irfunction.addInstr(CRET(irgen(node.expr, irprogram, irfunction)))
    elif isinstance(node, AssignStmt):
        # get the left side of an assigment
        src = irgen(node.lvalue, irprogram, irfunction)
        dest = irgen(node.expr, irprogram, irfunction)
        irfunction.addInstr(CASSGN(src, dest))

    else:
        for x in node.children():
            irgen(x, irprogram, irfunction)

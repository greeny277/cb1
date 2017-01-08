""" module for generating intermediate code """

import json
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
        CBRA, \
        CBEQ, \
        CBNE, \
        CBGT, \
        CBGE, \
        CBLT, \
        CBLE, \
        CCALL, \
        CRET, \
        CASSGN, \
        CSTORE

from ast import \
        Program, \
        VarDecl, \
        Function, \
        Block, \
        Identifier, \
        Type, \
        AssignStmt, \
        ReturnStmt, \
        IfStmt, \
        WhileStmt, \
        LValue, \
        IntLiteral, \
        FloatLiteral, \
        Literal, \
        ArithExpr, \
        CondExpr, \
        FuncCall, \
        ToReal, \
        ToInt

# TODO check default value for parameter


# Parameters:
#   node: LValue
def getBase(node, irprogram, irfunction):
    base = None
    irvar = node.name.decl.getIRVar()
    if irvar is not None:
        base = irvar
    else:
        print("ERROR LValue: Cant find IRVariable object to identifier")
    return base


def getOffset(node):
    decl = node.name.getDecl()
    derefs = decl.array
    offset = 0
    dims = node.name.getDecl().getArray()
    # compute index for 1-dim array storage
    for i in range(0, len(derefs)):
            for j in range(i+1, len(dims)):
                offset += derefs[i]*dims[j]

    offset += derefs[len(derefs)-1]
    return offset


def irgen(node, irprogram=None, irfunction=None, jump_dest=None, jump_right=None, negation=False):
    if isinstance(node, Program):
        irprogram = IRProgram()
        for v in node.vars:  # TODO use addGlobal(?)
            # Create IRVariable for globale variables
            irvar = irprogram.getIRVar(v.name.name, v.type)
            irprogram.variables.append(irvar)
            v.setIRVar(irvar)
        for f in node.funcs:  # TODO use addFunc(?)
            irprogram.functions.append(irgen(f, irprogram))
        return irprogram
    elif isinstance(node, Function):
        irfunction = IRFunction(node.name.name, irprogram)
        for par in node.arglist:
            irpar = irprogram.getIRVar(par.name.name, par.type)
            irfunction.addParam(irpar)
            par.setIRVar(irpar)
        irgen(node.block, irprogram, irfunction)
        return irfunction
    elif isinstance(node, VarDecl):
        # Edited: node.name to node.name.name
        irvar = irprogram.getIRVar(node.name.name, node.type)
        node.setIRVar(irvar)
        irfunction.addVar(irvar)
    elif isinstance(node, Block):
        for x in node.children():
            irgen(x, irprogram, irfunction)
    elif isinstance(node, Identifier):
        if node.decl.getIRVar() is not None:
            return node.decl.getIRVar()
        else:
            print("ERROR Identifier: Cant find IRVariable object to identifier")
    elif isinstance(node, ToInt):
        tmp = irgen(node.successor, irprogram, irfunction)
        virtReg = irprogram.getFreeVirtReg(irfunction, Type.getIntType())
        irfunction.addInstr(CR2I(virtReg, tmp))
        irfunction.virtRegs[virtReg.name] = virtReg
        return virtReg
    elif isinstance(node, ToReal):
        tmp = irgen(node.successor, irprogram, irfunction)
        virtReg = irprogram.getFreeVirtReg(irfunction, Type.getRealType())
        irfunction.addInstr(CR2I(virtReg, tmp))
        irfunction.virtRegs[virtReg.name] = virtReg
        return virtReg
    elif isinstance(node, Literal):
        return ConstValue(node.val, node.type)
    elif isinstance(node, LValue):
        decl = node.name.getDecl()
        derefs = None
        if isinstance(decl, Identifier):
            derefs = decl.getArrayDeref()
        else:
            derefs = decl.array

        if len(derefs) != 0:
            # is array
            virtReg = irprogram.getFreeVirtReg(irfunction, decl.type.getBaseType())
            base = getBase(node, irprogram, irfunction)
            offset = getOffset(node)
            irfunction.addInstr(CLOAD(virtReg, base, offset))
            return virtReg
        else:
            return irgen(node.name, irprogram, irfunction)

    elif isinstance(node, ArithExpr):
        # Evaluate leftern subtree
        leftReg = irgen(node.left, irprogram, irfunction)
        # Evaluate rightern subtree
        rightReg = irgen(node.right, irprogram, irfunction)

        if rightReg.type != leftReg.type:
            print("ArithExpr: Subexpressions have different type :'(")

        destReg = irprogram.getFreeVirtReg(irfunction, rightReg.type)

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
            virtReg = irgen(p, irprogram, irfunction)
            irfunction.addInstr(CPUSH(virtReg))

        # get the return type of the func call
        returnType = node.func_name.getDecl().getType()
        destReg = irprogram.getFreeVirtReg(irfunction, returnType)
        irfunction.addInstr(CCALL(destReg, node.func_name.name))
        return destReg
    elif isinstance(node, ReturnStmt):
        irfunction.addInstr(CRET(irgen(node.expr, irprogram, irfunction)))
    elif isinstance(node, CondExpr):
        if node.op.val == "||":
            l_right_cond = irprogram.genLabel()
            irgen(node.left, irprogram, irfunction, jump_dest, l_right_cond)
            irfunction.addInstr(l_right_cond)
            irgen(node.right, irprogram, irfunction, jump_dest, jump_right)
            irfunction.addInstr(CBRA(jump_right))
        elif node.op.val == "&&":
            l_right_cond = irprogram.genLabel()
            irgen(node.left, irprogram, irfunction, jump_dest, l_right_cond, True)
            irfunction.addInstr(l_right_cond)
            irgen(node.right, irprogram, irfunction, jump_dest, jump_right)
            irfunction.addInstr(CBRA(jump_right))
        # Evaluate rightern subtree
        else:
            leftReg = irgen(node.left, irprogram, irfunction)
            rightReg = irgen(node.right, irprogram, irfunction)
            if node.op.val == "<=":
                if negation:
                    irfunction.addInstr(CBGT(jump_right, leftReg, rightReg))
                else:
                    irfunction.addInstr(CBLE(jump_dest, leftReg, rightReg))
            elif node.op.val == "=":
                if negation:
                    irfunction.addInstr(CBNE(jump_right, leftReg, rightReg))
                else:
                    irfunction.addInstr(CBEQ(jump_dest, leftReg, rightReg))
            elif node.op.val == "!=":
                if negation:
                    irfunction.addInstr(CBEQ(jump_right, leftReg, rightReg))
                else:
                    irfunction.addInstr(CBNE(jump_dest, leftReg, rightReg))
            elif node.op.val == "<":
                if negation:
                    irfunction.addInstr(CBGE(jump_right, leftReg, rightReg))
                else:
                    irfunction.addInstr(CBLT(jump_dest, leftReg, rightReg))
            elif node.op.val == ">":
                if negation:
                    irfunction.addInstr(CBLE(jump_right, leftReg, rightReg))
                else:
                    irfunction.addInstr(CBGT(jump_dest, leftReg, rightReg))
            elif node.op.val == ">=":
                if negation:
                    irfunction.addInstr(CBLT(jump_right, leftReg, rightReg))
                else:
                    irfunction.addInstr(CBGE(jump_dest, leftReg, rightReg))

    elif isinstance(node, IfStmt):
        l_then = irprogram.genLabel()
        l_else = irprogram.genLabel()
        irgen(node.cond, irprogram, irfunction, l_then, l_else)
        irfunction.addInstr(l_then)
        irgen(node.trueblock, irprogram, irfunction)
        irfunction.addInstr(l_else)
        irgen(node.falseblock, irprogram, irfunction)
    elif isinstance(node, WhileStmt):
        l_cond = irprogram.genLabel()
        l_then = irprogram.genLabel()
        l_end = irprogram.genLabel()
        irfunction.addInstr(l_cond)
        irgen(node.cond, irprogram, irfunction, l_then, l_end)
        irfunction.addInstr(l_then)
        irgen(node.block, irprogram, irfunction)
        irfunction.addInstr(CBRA(l_cond))
        irfunction.addInstr(l_end)
    elif isinstance(node, AssignStmt):
        # get the left side of an assigment
        src = irgen(node.expr, irprogram, irfunction)
        decl = node.lvalue.name.getDecl()
        derefs = decl.array
        if len(derefs) != 0:
            # is array
            base = getBase(node.lvalue, irprogram, irfunction)
            offset = getOffset(node.lvalue)
            irfunction.addInstr(CSTORE(src, base, offset))
        else:
            dest = irgen(node.lvalue, irprogram, irfunction)
            irfunction.addInstr(CASSGN(src, dest))
    else:
        for x in node.children():
            irgen(x, irprogram, irfunction)

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


def getBase(node, irfunction):
    base = None
    if node.name.name in irfunction.vars:
        base = irfunction.vars[node.name.name]
    elif node.name.name in irfunction.params:
        base = irfunction.params[node.name.name]
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
            irprogram.variables.append(irgen(v))

        for f in node.funcs:  # TODO use addFunc(?)
            irprogram.functions.append(irgen(f, irprogram))
    elif isinstance(node, Function):
        irfunction = IRFunction(node.name.name, irprogram)
        for par in node.arglist:
            irpar = irprogram.getIRVar(par.name.name, par.type)
            irfunction.addParam(irpar)
        irgen(node.block, irprogram, irfunction)
    elif isinstance(node, VarDecl):
        # Edited: node.name to node.name.name
        irvar = irprogram.getIRVar(node.name.name, node.type)
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
            print("ERROR Identifier: Cant find IRVariable object to identifier")
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
        derefs = None
        if isinstance(decl, Identifier):
            derefs = decl.getArrayDeref()
        else:
            derefs = decl.array

        if len(derefs) != 0:
            # is array
            virtReg = irprogram.getFreeVirtReg(decl.type.getBaseType())
            base = getBase(node, irfunction)
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
                    irfunction.addInstr(CBGT(leftReg, rightReg, jump_right))
                else:
                    irfunction.addInstr(CBLE(leftReg, rightReg, jump_dest))
            elif node.op.val == "=":
                if negation:
                    irfunction.addInstr(CBNE(leftReg, rightReg, jump_right))
                else:
                    irfunction.addInstr(CBEQ(leftReg, rightReg, jump_dest))
            elif node.op.val == "<":
                if negation:
                    irfunction.addInstr(CBGE(leftReg, rightReg, jump_right))
                else:
                    irfunction.addInstr(CBLT(leftReg, rightReg, jump_dest))
            elif node.op.val == ">":
                if negation:
                    irfunction.addInstr(CBLE(leftReg, rightReg, jump_right))
                else:
                    irfunction.addInstr(CBGT(leftReg, rightReg, jump_dest))
            elif node.op.val == ">=":
                if negation:
                    irfunction.addInstr(CBLT(leftReg, rightReg, jump_right))
                else:
                    irfunction.addInstr(CBGE(leftReg, rightReg, jump_dest))

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
            dest = irprogram.getFreeVirtReg(decl.type.getBaseType())
            base = getBase(node.lvalue, irfunction)
            offset = getOffset(node.lvalue)
            irfunction.addInstr(CSTORE(dest, base, offset))
        else:
            dest = irgen(node.lvalue, irprogram, irfunction)
            irfunction.addInstr(CASSGN(src, dest))
    else:
        for x in node.children():
            irgen(x, irprogram, irfunction)

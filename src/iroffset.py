from ir import \
        IRProgram, \
        IRFunction, \
        IRVariable, \
        CUnary, \
        CCondBranch, \
        VirtualRegister, \
        CSTORE, \
        CLOAD, \
        CCALL, \
        CBinary


def iroffset(node, curOffset=None):
    if isinstance(node, IRProgram):
        for x in node.functions:
            iroffset(x, 0)
    elif isinstance(node, IRFunction):
        paramOffset = 8
        for param in node.params.values():
            paramOffset += 8
            param.offset = paramOffset
            print("Param:" + str(node) + " has offset: " + str(param.offset))
        tmpOffset = 0
        for v in node.vars.values():
            tmpOffset = iroffset(v, tmpOffset)
        for virt in node.virtRegs.values():
            tmpOffset = iroffset(virt, tmpOffset)
    elif isinstance(node, IRVariable) or \
            isinstance(node, VirtualRegister):
        if isinstance(node, IRVariable) and node.isGlobal:
            return curOffset
        if node.offset is None:
            if node.type.isPrimitive():
                curOffset -= 8
                node.offset = curOffset
            else:
                dimSize = 1
                for dim in node.type.getSimpleDimList():
                    dimSize *= dim
                curOffset -= 8*dimSize
                node.offset = curOffset
            print("LocalVar: " + str(node) + " has offset: " + str(node.offset))

        return curOffset
    else:
        return curOffset

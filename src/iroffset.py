from ir import \
        IRProgram, \
        IRFunction, \
        IRVariable, \
        CUnary, \
        CCondBranch, \
        VirtualRegister, \
        CSTORE, \
        CLOAD, \
        CBinary


def iroffset(node, curOffset=None):
    if isinstance(node, IRProgram):
        for x in node.functions:
            iroffset(x, 0)
    elif isinstance(node, IRFunction):
        paramOffset = 0
        for param in node.params.values():
            paramOffset += 8
            param.offset = paramOffset
            #print("Param:" + str(node) + " has offset: " + str(param.offset))
        tmpOffset = 0
        for x in node.instrs():
            tmpOffset = iroffset(x, tmpOffset)
    elif isinstance(node, IRVariable) or \
            isinstance(node, VirtualRegister):
        if node.offset is None:
            curOffset -= 8
            node.offset = curOffset
            #print("LocalVar: " + str(node) + " has offset: " + str(node.offset))
        return curOffset
    elif isinstance(node, CBinary) or \
            isinstance(node, CCondBranch):
        tmpOffset = iroffset(node.left.val, curOffset)
        return iroffset(node.right.val, tmpOffset)
    elif isinstance(node, CLOAD):
        tmpOffset = iroffset(node.target.val, curOffset)
        tmpOffset = iroffset(node.base.val, tmpOffset)
        return iroffset(node.offset.val, tmpOffset)
    elif isinstance(node, CSTORE):
        tmpOffset = iroffset(node.target.val, curOffset)
        tmpOffset = iroffset(node.offset.val, tmpOffset)
        return iroffset(node.offset.val, tmpOffset)
    elif isinstance(node, CUnary):
        tmpOffset = iroffset(node.source.val, curOffset)
        return iroffset(node.target.val, tmpOffset)
    else:
        return curOffset

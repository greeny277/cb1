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
            iroffset(x)
    elif isinstance(node, IRFunction):
        offset = 0
        for param in node.params.values():
            offset += 8
            param.offset = offset
        for x in node.instrs():
            iroffset(x, 0)
    elif isinstance(node, IRVariable) or \
            isinstance(node, VirtualRegister):
        if node.offset is None:
            curOffset -= 8
            node.offset = curOffset
        return curOffset
    elif isinstance(node, CBinary) or \
            isinstance(node, CCondBranch):
        tmpOffset = iroffset(node.left.val, curOffset)
        return iroffset(node.right.val, tmpOffset)
    elif isinstance(node, CSTORE):
        tmpOffset = iroffset(node.target.val, curOffset)
        tmpOffset = iroffset(node.base.val, tmpOffset)
        return iroffset(node.offset.val, tmpOffset)
    elif isinstance(node, CLOAD):
        tmpOffset = iroffset(node.target.val, curOffset)
        tmpOffset = iroffset(node.offset.val, tmpOffset)
        return iroffset(node.offset.val, tmpOffset)
    elif isinstance(node, CUnary):
        tmpOffset = iroffset(node.source.val, curOffset)
        return iroffset(node.target.val, tmpOffset)

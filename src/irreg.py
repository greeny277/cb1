import ast
from ir import \
        IRProgram, \
        IRFunction, \
        IRVariable, \
        ConstValue, \
        CCondBranch, \
        HardwareRegister, \
        OperandValue, \
        CUnary, \
        CLOAD, \
        CBinary,\
        CPUSH, \
        CMUL, \
        CADD, \
        CSUB, \
        CDIV, \
        CBRA, \
        CBEQ, \
        CBNE, \
        CBGT, \
        CBGE, \
        CBLT, \
        CBLE, \
        CCALL, \
        CI2R, \
        CR2I, \
        CRET, \
        CASSGN, \
        CSTORE

from common import InternalError, Type


def irreg(node, hw_registers=None, hw_register=None, iCode=None):
    if isinstance(node, IRProgram):
        # Create HW-Registers
        hw_registers = {}
        for name in ['rax', 'rcx', 'rdx', 'rbx', 'rsi', 'rdi']:
            hw_registers[name] = HardwareRegister(name, Type.getIntType())
        for x in node.functions:
            irreg(x, hw_registers)
    elif isinstance(node, IRFunction):
        for x in node.instrs():
            irreg(x, hw_registers)

    elif isinstance(node, OperandValue):
        # Someone uses a variable, we need to make sure
        # it is in a real register
        iCode.insertBefore(CASSGN(hw_register, node))
        return hw_register
    elif isinstance(node, CBinary):
        l = irreg(node.left.val,  None, hw_registers['rax'], node)
        r = irreg(node.right.val, None, hw_registers['rcx'], node)
        if l is None:
            l = node.left.val
        if r is None:
            r = node.right.val
        if isinstance(node, CMUL):
            node.insertBefore(CMUL(hw_registers['rax'], l, r))
        elif isinstance(node, CADD):
            node.insertBefore(CADD(hw_registers['rax'], l, r))
        elif isinstance(node, CSUB):
            node.insertBefore(CSUB(hw_registers['rax'], l, r))
        elif isinstance(node, CDIV):
            node.insertBefore(CDIV(hw_registers['rax'], l, r))
        node.insertBefore(CASSGN(node.target.val, hw_registers['rax']))
        node.remove()
    elif isinstance(node, CUnary):
        irreg(node.source.val, None, hw_registers['rax'], node)
        if isinstance(node, CASSGN):
            node.insertBefore(CASSGN(node.target.val, hw_registers['rax']))
        elif isinstance(node, CI2R):
            node.insertBefore(CI2R(node.target.val, hw_registers['rax']))
        elif isinstance(node, CR2I):
            node.insertBefore(CR2I(node.target.val, hw_registers['rax']))
        node.remove()
    elif isinstance(node, CCondBranch):
        l = irreg(node.left.val, None, hw_registers['rax'], node)
        r = irreg(node.right.val, None, hw_registers['rcx'], node)
        if isinstance(node, CBEQ):
            node.insertBefore(CBEQ(node.label, l, r))
        if isinstance(node, CBGE):
            node.insertBefore(CBGE(node.label, l, r))
        if isinstance(node, CBGT):
            node.insertBefore(CBGT(node.label, l, r))
        if isinstance(node, CBLE):
            node.insertBefore(CBLE(node.label, l, r))
        if isinstance(node, CBLT):
            node.insertBefore(CBLT(node.label, l, r))
        if isinstance(node, CBNE):
            node.insertBefore(CBNE(node.label, l, r))
        node.remove()
    elif isinstance(node, CSTORE):
        v = irreg(node.value.val, None, hw_registers['rax'], node)
        node.insertBefore(CSTORE(node.target.val, node.offset.val, v))
        node.remove()
    elif isinstance(node, CLOAD):
        t = irreg(node.target.val, None, hw_registers['rax'], node)
        node.insertBefore(CLOAD(t, node.base.val, node.offset.val))
    else:
        return None


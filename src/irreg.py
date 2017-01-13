import ast
from ir import \
        IRProgram, \
        IRFunction, \
        IRVariable, \
        ConstValue, \
        HardwareRegister, \
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
        CRET, \
        CASSGN, \
        CSTORE

from common import InternalError, Type


def irreg(node, hw_registers=None, hw_register=None):
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

    elif isinstance(node, IRVariable):
        # Someone uses a variable, we need to make sure
        # it is in a real register
        node.insertBefore(CASSGN(hw_register, node))
    elif isinstance(node, CBinary):
        irreg(node.left, None, hw_registers['rax'])
        irreg(node.right, None, hw_registers['rcx'])
        if isinstance(node, CMUL):
            node.insertBefore(CMUL(hw_registers['rax'], hw_registers['rax'], hw_registers['rcx']))
        elif isinstance(node, CADD):
            node.insertBefore(CADD(hw_registers['rax'], hw_registers['rax'], hw_registers['rcx']))
        elif isinstance(node, CSUB):
            node.insertBefore(CSUB(hw_registers['rax'], hw_registers['rax'], hw_registers['rcx']))
        elif isinstance(node, CDIV):
            node.insertBefore(CDIV(hw_registers['rax'], hw_registers['rax'], hw_registers['rcx']))
        node.insertBefore(CASSGN(node.target, hw_registers['rax']))
        node.remove()

    else:
        for x in node.children():
            irreg(x, hw_registers)

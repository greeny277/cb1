import ast
from ir import \
        IRProgram, \
        IRFunction, \
        IRVariable, \
        ConstValue, \
        CCondBranch, \
        HardwareRegister, \
        VirtualRegister, \
        OperandValue, \
        CUnary, \
        CLOAD, \
        CBinary,\
        CLABEL,\
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


calling_convention = ["rdi, rsi, rdx, rcx, r8, r9"]
caller_save = calling_convention + ["rax", "r10", "r11"]
callee_save = ["rbx", "rbp", "r12", "r13", "r14", "r15"]


def print_debug(node, asmfile):
    asmfile.write("# " + node.prettyprint())


def asmgen(node, asmfile, filename=None):
    print_debug(node, asmfile)
    if isinstance(node, IRProgram):
        asmfile.write(".file\t\"" + filename + "\"\n")
        asmfile.write(".intel_syntax noprefix")
        asmfile.write(".text")

        for func in node.functions:
            asmfile.write(func.name + ":\n")
            asmgen(func, asmfile, filename)

        for globVar in node.variables:
            asmfile.write(".lcomm\t" + globVar.name + ", 8\n")
    elif isinstance(node, CPUSH):
        asmfile.write("push\t" + str(node.source))
    elif isinstance(node, CCALL):
        asmfile.write("call\t" + node.name + "\n")
    elif isinstance(node, CRET):
        asmfile.write("mov\t" + "rax," + str(node.source.val) + "\n")
        asmfile.write("pop rbp\n")
        asmfile.write("ret\n")
    elif isinstance(node, CCondBranch):
        if isinstance(node, CLABEL):
            asmfile.write(str(node.label) + ":\n")
        left = str(node.left)[1:]
        right = str(node.left)[1:]
        asmfile.write("cmp\t" + left + "," + right + "\n")
        if isinstance(node, CBEQ):
            asmfile.write("je\t" + str(node.label) + "\n")
        if isinstance(node, CBGE):
            asmfile.write("jge\t" + str(node.label) + "\n")
        if isinstance(node, CBGT):
            asmfile.write("jg\t" + str(node.label)+"\n")
        if isinstance(node, CBLE):
            asmfile.write("jle\t" + str(node.label) + "\n")
        if isinstance(node, CBLT):
            asmfile.write("jl\t" + str(node.label) + "\n")
        if isinstance(node, CBNE):
            asmfile.write("jne\t" + str(node.label) + "\n")
    elif isinstance(node, IRFunction):
        asmfile.write("push\trbp\n")
        asmfile.write("mov\trbp, rsp\n")
        stackFrame = 8 * (len(node.vars) + len(node.virtRegs))
        if stackFrame > 0:
            asmfile.write("sub\trsp, " + str(stackFrame))
        for instr in node.instrs():
            asmgen(instr, asmfile)

    elif isinstance(node, CBinary):
        if isinstance(node, CDIV):
            asmfile.write("cdq\n")
            asmfile.write("idiv\t")

        elif isinstance(node, CADD):
            asmfile.write("add\t")
        elif isinstance(node, CSUB):
            asmfile.write("sub\t")
        elif isinstance(node, CMUL):
            asmfile.write("imul\t")

        asmgen(node.left, asmfile)
        asmfile.write(", ")
        asmgen(node.right, asmfile)
        asmfile.write("\n")
    elif isinstance(node, CUnary):
        asmfile.write("mov\t")
        asmgen(node.target, asmfile)
        asmfile.write(", ")
        asmgen(node.source, asmfile)
        asmfile.write("\n")
    elif isinstance(node, VirtualRegister) or isinstance(node, IRVariable):
        if node.offset < 0:
            asmfile.write("[rbp" + str(node.offset) + "]")
        else:
            asmfile.write("[rbp+" + str(node.offset) + "]")
    elif isinstance(node, OperandValue):
        asmfile.write(str(node.name))

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
param_counter = 0


def print_debug(node, asmfile):
    asmfile.write("\t# " + str(node) + "\n")



def asmgen(node, asmfile, filename=None):
    if not isinstance(node, OperandValue):
        print_debug(node, asmfile)
        if not isinstance(node, CLABEL):
            asmfile.write("\t")
    if isinstance(node, IRProgram):
        asmfile.write(".file\t\"" + filename + "\"\n")
        asmfile.write("\t.intel_syntax noprefix\n")
        asmfile.write("\t.text\n")
        asmfile.write("\t.global\t_start")
        for func in node.functions:
            if func.name == "mod":
                asmfile.write(", mod_0")
            else:
                asmfile.write(", " + func.name)
        asmfile.write("\n")

        asmfile.write("_start:\n")
        asmfile.write("\tcall\tmain\n")
        asmfile.write("\tmov\tebx, eax\n")
        asmfile.write("\tmov\teax, 1\n")
        asmfile.write("\tint\t0x80\n")
        for func in node.functions:
            if func.name == "mod":
                asmfile.write("mod_0:\n")
            else:
                asmfile.write(func.name + ":\n")
            asmgen(func, asmfile, filename)

        for globVar in node.variables:
            if globVar.type.isPrimitive():
                asmfile.write(".lcomm\t" + globVar.name + ", 8\n")
            else:
                dimSize = 1
                for dim in globVar.type.getSimpleDimList():
                    dimSize *= dim
                dimSize *= 8
                asmfile.write(".lcomm\t" + globVar.name + ", " + str(dimSize) + "\n")

    elif isinstance(node, CPUSH):
        global param_counter
        param_counter += 1

        if isinstance(node.next, CCALL):
            if node.next.name == "writeChar" or node.next.name == "writeInt":
                asmfile.write("mov rdi, ")
                asmgen(node.source.val, asmfile)
                asmfile.write("\n")
                return

        asmfile.write("push\t")
        asmgen(node.source.val, asmfile)
        asmfile.write("\n")
    elif isinstance(node, CCALL):
        if node.name == "time":
            asmfile.write("call\tmy_time\n")
        elif node.name == "mod":
            asmfile.write("call\tmod_0\n")
        else:
            asmfile.write("call\t" + node.name + "\n")
        asmfile.write("\tmov\t")
        asmgen(node.target.val, asmfile)
        asmfile.write(", rax\n")
        global param_counter
        if param_counter >= 1 and node.name != "writeChar" and node.name != "writeInt":
            asmfile.write("\tadd rsp, " + str(8*param_counter) + "\n")
        param_counter = 0
    elif isinstance(node, CRET):
        asmfile.write("mov\t" + "rax, ")
        asmgen(node.source.val, asmfile)
        asmfile.write("\n")
        asmfile.write("\tleave\n")
        asmfile.write("\tret\n")
    elif isinstance(node, CLABEL):
        asmfile.write("." + str(node) + "\n")
    elif isinstance(node, CBRA):
        asmfile.write("jmp\t." + str(node.label)[:-1] + "\n")
    elif isinstance(node, CCondBranch):
        asmfile.write("cmp\t")
        asmgen(node.left.val, asmfile)
        asmfile.write(", ")
        asmgen(node.right.val, asmfile)
        asmfile.write("\n")
        if isinstance(node, CBEQ):
            asmfile.write("\tje\t." + str(node.label)[:-1] + "\n")
        if isinstance(node, CBGE):
            asmfile.write("\tjge\t." + str(node.label)[:-1] + "\n")
        if isinstance(node, CBGT):
            asmfile.write("\tjg\t." + str(node.label)[:-1]+"\n")
        if isinstance(node, CBLE):
            asmfile.write("\tjle\t." + str(node.label)[:-1] + "\n")
        if isinstance(node, CBLT):
            asmfile.write("\tjl\t." + str(node.label)[:-1] + "\n")
        if isinstance(node, CBNE):
            asmfile.write("\tjne\t." + str(node.label)[:-1] + "\n")
    elif isinstance(node, IRFunction):
        asmfile.write("push\trbp\n")
        asmfile.write("\tmov\trbp, rsp\n")
        stackFrame = 8 * len(node.virtRegs)
        for locVar in node.vars.values():
            if locVar.type.isPrimitive():
                stackFrame += 8
            else:
                dimSize = 1
                for dim in locVar.type.getSimpleDimList():
                    dimSize *= dim
                stackFrame += 8*dimSize
        if stackFrame > 0:
            asmfile.write("\tsub\trsp, " + str(stackFrame) + "\n")
        while stackFrame > 0:
            asmfile.write("\tmov QWORD PTR [rbp-" + str(stackFrame) + "], 0\n")
            stackFrame -= 8
        for instr in node.instrs():
            asmgen(instr, asmfile)

    elif isinstance(node, CBinary):
        if isinstance(node, CDIV):
            asmfile.write("cqo\n")
            asmfile.write("\tidiv\t")

        elif isinstance(node, CADD):
            asmfile.write("add\t")
        elif isinstance(node, CSUB):
            asmfile.write("sub\t")
        elif isinstance(node, CMUL):
            asmfile.write("imul\t")

        asmgen(node.left.val, asmfile)
        asmfile.write(", ")
        asmgen(node.right.val, asmfile)
        asmfile.write("\n")
    elif isinstance(node, VirtualRegister) or isinstance(node, IRVariable):
        if node.offset is None:
            asmfile.write(str(node))
        elif node.offset < 0:
            asmfile.write("[rbp" + str(node.offset) + "]")
        else:
            asmfile.write("[rbp+" + str(node.offset) + "]")
    elif isinstance(node, OperandValue):
        asmfile.write(str(node))
    elif isinstance(node, CSTORE):
        asmfile.write("mov rbx, ")
        asmgen(node.offset.val, asmfile)
        asmfile.write("\n")
        asmfile.write("\tlea rsi,")
        asmgen(node.target.val, asmfile)
        asmfile.write("\n")
        asmfile.write("\tmov [rsi + rbx*0x8], ")
        asmgen(node.value.val, asmfile)
        asmfile.write("\n")
    elif isinstance(node, CLOAD):
        asmfile.write("mov rbx, ")
        asmgen(node.offset.val, asmfile)
        asmfile.write("\n")
        asmfile.write("\tlea rsi,")
        asmgen(node.base.val, asmfile)
        asmfile.write("\n")
        asmfile.write("\tmov rbx, [rsi + rbx*0x8]\n")
        asmfile.write("\tmov ")
        asmgen(node.target.val, asmfile)
        asmfile.write(", rbx\n")
    elif isinstance(node, CUnary):
        asmfile.write("mov\t")
        asmgen(node.target.val, asmfile)
        asmfile.write(", ")
        asmgen(node.source.val, asmfile)
        asmfile.write("\n")

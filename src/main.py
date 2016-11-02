#! /usr/bin/python3
"""main module"""

import e_parser
import argparse
import os
import sys
import dumpAST
import common
import dumpDot

from common import InputError

args = None

# source directory of python e compiler
MyDirectory = common.sourceDirectory

# source of e runtime functions (if needed)
RuntimeSrcFile = MyDirectory + "/sys.e"

# object file containing compiled e runtime functions (if needed)
RuntimeObjFile = MyDirectory + "/sys.o"


# argument parser object
parser = argparse.ArgumentParser(description="e compiler (in python)")
parser.add_argument('-o', help="output file", nargs=1, default=["a.out"],
                    metavar="<outputFile>")
parser.add_argument('-S', help="Just generate assembler",
                    action='store_true', default=False)
parser.add_argument('-c', help="Do not call the linker",
                    action='store_true', default=False)
parser.add_argument('--keep', help="do not delete temporary files",
                    action='store_true', default=False)
parser.add_argument('--dump-ast', help="dump AST", action='store_true',
                    default=False)
parser.add_argument('--dump-all', help="activate all dumps", action='store_true',
                    default=False)
parser.add_argument('--dump-cil', help="dump CIL", action='store_true', default=False)
parser.add_argument('-m', help="choose backend (x86|arm|amd64|jvm|...)", nargs=1,
                    default="amd64", metavar="<backend>")
parser.add_argument('inputfile', help="Input File", metavar="<inputFile>")
parser.add_argument('--dotify-ast', help="Generate a dot file out of a given source file", action='store_true',
                    default=False)

def main(arguments):
    """main function"""
    try:
        myargs = parser.parse_args(arguments)
        common.runtimeArgs = myargs

        # e source file name
        inputfile = myargs.inputfile
        assert inputfile.endswith('.e')
        inputfilebasename = inputfile[:-2]

        # file name of final program
        outputfile = myargs.o[0]

        # file name of temporary assembler file
        asmfile = inputfilebasename + ".S"

        # file name of temporary object file
        objfile = inputfilebasename + ".o"

        # file name of AST Dump
        astdumpfile = inputfilebasename + ".AST"

        # file name of CIL Dump
        cildumpfile = inputfilebasename + ".CIL"

        # file name of DOT Dump
        x = e_parser.doParsing(inputfile)

        # TODO: fold constants

        # TODO: resolve declarations

        # TODO: check types

        if myargs.dump_ast is not None:
            adf = open(astdumpfile, "w")
            adf.write("AST dump\n")
            # TODO: write AST to file object adf
            adf.close()

        if myargs.dotify_ast is not None:
            # TODO
            dotdumpfile = inputfilebasename + ".dot"
            ddf = open(dotdumpfile, "w")
            dumpDot.dump(x, ddf)
            ddf.close()

        # This ast dumping is for debugging purposes,
        # you may remove it.
        dumpAST.dump(x, sys.stdout)

        # TODO: intermediate code generation

        if myargs.dump_cil is not None:
            cdf = open(cildumpfile, "w")
            cdf.write("CIL code dump\n")
            # TODO: write IR code to file object cdf
            cdf.close()

        asmfd = open(asmfile, "w")
        asmfd.write("; python e compiler assembler\n")
        # TODO: assembler generation
        asmfd.close()

        # TODO: if needed, switch to compiling RuntimeSrcFile
        #       into RuntimeObjFile

        # TODO: run assembler, make it produce objfile from asmfile
        os.system("touch " + objfile)

        # TODO: run linker, make it produce outputfile from objfile
        #       and RuntimeObjFile
        os.system("touch " + outputfile)

        if not myargs.keep:
            # TODO: remove all temporary files
            pass
    except InputError as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])

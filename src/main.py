#! /usr/bin/env python3
"""main module"""

import e_parser
import argparse
import os
import sys
import dumpAST
import dumpDot
import common
import constFold
import symbolAST
import typeCheck
import irgen
import irser
import irreg
import iroffset
import asmgen

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
parser.add_argument('-S', help="Just generate assembler", nargs=1,
                    metavar="<outputFile>")
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
parser.add_argument('--dump-cil-to-file-and-exit', help="Dump the generated intermediate code",
        nargs=1, metavar="<cilFile>")

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
        if myargs.S is not None:
            asmfile = myargs.S[0] + ".S"

        # file name of temporary object file
        objfile = inputfilebasename + ".o"
        if myargs.o is not None:
            objfile = myargs.o[0] + ".o"

        # file name of AST Dump
        astdumpfile = inputfilebasename + ".AST"


        # file name of CIL Dump
        cildumpfile = inputfilebasename + ".CIL"

        # file name of DOT Dump
        x = e_parser.doParsing(inputfile)

        # This ast dumping is for debugging purposes,
        # you may remove it.
        #dumpAST.dump(x, sys.stdout)

        # initialize libriary functions
        lib = e_parser.doParsing(os.path.dirname(__file__) + '/libs/lib.e')
        if myargs.dotify_ast is not None:
            dotdumpfile = inputfilebasename + ".dot"
            ddf = open(dotdumpfile, "w")
            dumpDot.dumpDot(x, ddf)
            ddf.close()

        # fold constants
        constFold.foldingAST(x)

        if myargs.dotify_ast is not None:
            """ Save AST after const folding
            """
            dotdumpfile = inputfilebasename + ".simplfied" + ".dot"
            ddf = open(dotdumpfile, "w")
            dumpDot.dumpDot(x, ddf)
            ddf.close()

        # init the lib
        symbolAST.setLibAST(lib)

        # resolve declarations
        symbolAST.traverse(x)

        # check types
        typeCheck.typeChecking(x)

        if myargs.dotify_ast is not None:
            """ Save AST after const folding
            """
            dotdumpfile = inputfilebasename + ".typing" + ".dot"
            ddf = open(dotdumpfile, "w")
            dumpDot.dumpDot(x, ddf)
            ddf.close()

        # Generate intermediate representation
        irprogram = irgen.irgen(x)

        # Register distribution
        irreg.irreg(irprogram)

        # Compute offsets relative to framepointer
        iroffset.iroffset(irprogram)

        irprogram.prettyprint(sys.stdout)
        if myargs.dump_cil_to_file_and_exit is not None:
            # file name of specified CIL Dump file
            cildumpfile_spec = myargs.dump_cil_to_file_and_exit[0]

            cdf = open(cildumpfile_spec, "w")
            cdf.write(irser.serialize(irprogram))
            cdf.close()
            sys.exit(0)

        if myargs.dump_cil is not None:
            cdf = open(cildumpfile, "w")
            cdf.write("CIL code dump\n")
            cdf.write(irser.serialize(irprogram))
            cdf.close()


        if myargs.dump_ast is not None:
            adf = open(astdumpfile, "w")
            adf.write("AST dump\n")
            # TODO: write AST to file object adf
            adf.close()

        asmfd = open(asmfile, "w")
        asmfd.write("# python e compiler assembler\n")
        asmgen.asmgen(irprogram, asmfd, inputfile)
        # assembler generation
        asmfd.close()

        # TODO: if needed, switch to compiling RuntimeSrcFile
        #       into RuntimeObjFile
        #

        # Compile libs

        reader = os.path.dirname(__file__) + '/libs/reader.S'
        writer = os.path.dirname(__file__) + '/libs/writer.S'
        writeChar = os.path.dirname(__file__) + '/libs/writeChar.S'
        readChar = os.path.dirname(__file__) + '/libs/readChar.S'

        os.system("as -o " + os.path.dirname(__file__) + "/libs/readInt.o " + reader)
        readerObj = os.path.dirname(__file__) + '/libs/readInt.o'

        os.system("as -o " + os.path.dirname(__file__) + "/libs/writeInt.o " + writer)
        writerObj = os.path.dirname(__file__) + '/libs/writeInt.o'
        
        os.system("as -o " + os.path.dirname(__file__) + "/libs/writeChar.o " + writeChar)
        writeCharObj = os.path.dirname(__file__) + '/libs/writeChar.o'

        os.system("as -o " + os.path.dirname(__file__) + "/libs/readChar.o " + readChar)
        readCharObj = os.path.dirname(__file__) + '/libs/readChar.o'
        # if no args are given
        if myargs.S is not None:
            sys.exit(0)
        if myargs.o is not None:
            os.system("as -o " + objfile + " " + asmfile)
            os.system("ld -dynamic-linker /lib64/ld-linux-x86-64.so.2 -lc " + readCharObj + " " + writeCharObj + " "+ readerObj + " " +
                    writerObj + " " + objfile + " -o  " + myargs.o[0])
            sys.exit(0)

        # run assembler, make it produce objfile from asmfile
        os.system("as -o a.o " + asmfile)
        # run linker, make it produce outputfile from objfile
        #       and RuntimeObjFile
        os.system("ld -dynamic-linker /lib64/ld-linux-x86-64.so.2 -lc " + readCharObj + " " + writeCharObj + " " + readerObj + " " +
                writerObj + " a.o")

        if not myargs.keep:
            # TODO: remove all temporary files
            pass
    except InputError as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])

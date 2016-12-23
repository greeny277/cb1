#! /usr/bin/python3
"""main module"""

import argparse
import os
import sys
import subprocess

import common
import irser
import interp

from common import InputError

# argument parser object
parser = argparse.ArgumentParser(description="e interpreter (in python)")

parser.add_argument('file', help="CIL File to interpret")


def main(arguments):
    """main function"""
    args = parser.parse_args(arguments)
    common.runtimeArgs = args

    inputfile = args.file
        
    fd = open(inputfile, "r")
    ss = fd.read()
    cil = irser.deserialize(ss)
    return interp.interpret(cil)

if __name__ == '__main__':
    exit(main(sys.argv[1:]))

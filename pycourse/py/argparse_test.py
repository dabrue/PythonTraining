#!/bin/env python3
import argparse
import sys


parser=argparse.ArgumentParser(description="This is a test to see how it works")

# optional argument
parser.add_argument("-f","--foo",action="store_true",help="what?")
parser.add_argument("-v","--verbose",help="what what?",action="store_true")

# positional arguments
parser.add_argument("Filename1",help="file 1")
parser.add_argument("Filename2",help="file 2")

args=parser.parse_args(sys.argv[1:])
print(vars(args))
print(args.Filename2)


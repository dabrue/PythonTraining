#!/bin/env python3
import sys

inname = sys.argv[1]

try:
    f=open(inname,"r")
    lines=f.read()
except:
    sys.stderr.write("ERROR\n")
    sys.stderr.write(str(sys.exc_info()[0]))
    raise

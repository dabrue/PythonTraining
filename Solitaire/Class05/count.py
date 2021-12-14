#!/bin/env python3
"""
    Read in a list of output numbers from the Solitaire algorithm, count
    occurances, and output to a file. 
"""

__author__      = "Daniel A. Brue"
__email__       = "dabrue@us.ibm.com"

if (__name__ == "__main__"):
    import sys
    import numpy
    import argparse

    parser=argparse.ArgumentParser(description="Make a count file from Observations")
    parser.add_argument("-i","--input",dest="infilename",required=True,action="store",
        help="Input file")
    parser.add_argument("-o","--output",dest="outfilename",required=True,action="store",
        help="Output file")
    args=parser.parse_args()

    with open(args.infilename,"r") as f:
        data=f.readlines()

    for i in range(len(data)):
        data[i] = int(data[i])

    NObservations = len(data)

    N = max(data)

    # Count the single number occurances
    Singles = numpy.zeros((N+1),dtype=numpy.int)
    for i in range(NObservations):
        Singles[data[i]] += 1

    # Count the double number occurances
    Doubles = numpy.zeros([N+1,N+1],dtype=numpy.int)
    for i in range(1,NObservations):
        m = data[i-1]
        n = data[i]
        Doubles[m][n] += 1


    # Count the triple number occurances
    Triples = numpy.zeros([N+1,N+1,N+1],dtype=numpy.int)
    for i in range(2,NObservations):
        l = data[i-2]
        m = data[i-1]
        n = data[i]
        Triples[l][m][n] += 1

    # Now make an output file
    NSingles = len(Singles)
    NDoubles = NSingles**2
    NTriples = NSingles**3
    outf=open(args.outfilename,"w")
    outf.write("# SINGLES "+str(NSingles)+"\n")
    for i in range(NSingles):
        outf.write(str(i).rjust(6)+str(Singles[i]).rjust(13)+"\n")
    outf.write("\n")
    outf.write("# DOUBLES "+str(NDoubles)+"\n")
    for i in range(len(Doubles)):
        for j in range(len(Doubles[i])):
            outf.write(str(i).rjust(6)+str(j).rjust(6)+str(Doubles[i][j]).rjust(13)+"\n")
    outf.write("\n")
    outf.write("# TRIPLES "+str(NTriples)+"\n")
    for i in range(len(Triples)):
        stri=str(i).rjust(6)
        for j in range(len(Triples[i])):
            strj=str(j).rjust(6)
            for k in range(len(Triples[i][j])):
                strk=str(k).rjust(6)
                outf.write(stri+strj+strk+str(Triples[i][j][k]).rjust(13)+"\n")
                
    outf.close()

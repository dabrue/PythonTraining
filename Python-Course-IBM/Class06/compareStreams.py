#!/bin/env python3
"""
    Routine for comparing solitaire stream output from similar keys. For class
    purposes, this routine demonstrates the subprocess.check_output and 
    multiprocess pool modules

    For the purposes of analyzing Solitaire, this routine will create a Reference
    stream by assessing the first 1000 outputs from the algorithm with a null key, 
    i.e. a perfectly sorted initial deck. This routine then generates 1431 variants
    by swapping two cards in the deck (there are 1431 ways to do this), and then
    generates a list of 1431 outputs (each output 1000 elements long) for comparison
    to the Reference. The multiprocess.pool functions are used to run these in 
    parrallel, and the subprocess.check_output is used to call an external routine
    that generates the output lists. 

    Once we have the Reference output and list of variation outputs, the routine
    then plots some of the comparisons that can be made. 

    The first plot is a count of first differences. Say that a given output stream
    is the same as the Reference stream for the first 20 elements, and differs on 
    the 21st; the first index of difference for these two streams is 21. At a
    value X=21, we increment Y(21) by one, and then compare the next stream. This 
    gives us a plot of how many of the 1431 streams first differ from the reference
    at a given index. If Y=42 at X=5, then 42 of the 1431 variants first differ
    from the Reference at index 5. 

    The second plot is a count of how many of the variant streams share the same
    output value in the same position as the reference stream. If a single variant
    has an output value of 20 at index 10, and this matches what the Reference has
    at index 10, then the count for X=10 is incremented by one. So if after all
    variants have been checked we have a value of Y=34 at X=15, then 34 of the
    1431 variants have the same card at index 15 as the Reference. Unlike the
    first plot, this one should not go to zero as X increases because even in a 
    comparison of perfectly random sequences, there is a chance that two sequences
    will have the same value at a given spot. Since there are 54 possible values
    the chance that one matches the other is 1/54. Since we have 1431 variants, the
    count at large X should be around 1431/54 = 26.5. 

    What we see in the second plot is that for small index values, there is a much
    higher number of variants that have the same (index,card) pair as the Reference. 
    This is not surprising since the intial deck orders are very similar, and what
    it says of the algorithm is that small changes in the initial ordering do not
    diffuse through the algorithm immediately. 
"""

__author__      = "Daniel A. Brue"
__email__       = "danielbrue@gmail.com"

import subprocess
import re

class StreamPair:
    def __init__(self,streamA, streamB):
        self.A = streamA
        self.B = streamB

def getSolOutput(solargs):
    """
        Call a subprocess to run the FORTRAN solitaire code and collect the output
    """

    # check_output calls an external function, collects and returns the output
    output = subprocess.check_output(solargs,stdin=None,stderr=None)
    # The output comes as a byte string. To make it a standard string for cleanup
    # we need to decode the byte string. 
    output = output.decode(encoding="UTF-8")
    output = re.sub("\n"," ",output)   # remove all new-lines from Fortran's print 
    outlist = output.split()  # split the single string into a list of strings
    outnum = []
    for i in range(len(outlist)):
        outnum.append(int(outlist[i]))
    return outnum   # return list of integers


def getDistances(S):
    """
        Find the first place where two streams differ, and the total number
        of identically places outputs
    """
    count=0
    differences=[]
    for i in range(len(S.A)):
        if (S.A[i] == S.B[i]):
            count+=1
        else:
            differences.append(i)

    return [count, differences]


if (__name__ == "__main__"):

    import multiprocessing
    import matplotlib.pyplot as plt

    SampleSize = 1000


    # Get a reference output. Null Key. The reference stream is the output from the
    # solitaire cipher with no key at all. This will be used for comparisons against
    # streams generated from slightly different initial decks. 
    Input = ["./solstream",str(SampleSize)]
    Deck = list(range(1,55))
    strDeck=[]
    for i in Deck:
        strDeck.append(str(i))
    NullDeck = []
    for i in range(len(Deck)):
        NullDeck.append(str(Deck[i]))
    solargs = Input + NullDeck
    Reference = getSolOutput(solargs)

    # Generate a list of varied starting points, swapping two cards
    Inputs=[]
    for i in range(53):
        for j in range(i+1,54):
            D=list(strDeck)
            tmp=D[j]
            D[j]=D[i]
            D[i]=tmp
            I=Input+D
            Inputs.append(I)
            
    print("Number of inputs is ",len(Inputs))


    # Generate a pool of processors to use. 
    # If NProc is set to None, then by default the pool command will use as 
    # many as it finds. 
    NProcessors = 4
    pool = multiprocessing.Pool(NProcessors)


    # Next we use the pool.map routine. For arguments we provide a function name
    # and a list of inputs to the function. The second argument must be a single
    # dimension iterable, but there is no restriction on the objects being
    # iterated over. Here, I am sending it a list of lists. 
    Outputs = pool.map(getSolOutput,Inputs)

    # Construct a list of stream pair objects, and pass it to map
    # This is one way to pass more complex data to a subroutine in a single argument
    StreamsList=[]
    for i in range(len(Outputs)):
        S = StreamPair(Reference,Outputs[i])
        StreamsList.append(S)

    Distances = pool.map(getDistances,StreamsList)


    # Now I'm going to histagram the distances and overlaps. First create some
    # zero filled arrays
    MinDiff = len(Reference)*[0]
    Overlaps= len(Reference)*[0]
    for Pair in Distances:
        Overlaps[Pair[0]] += 1
        MinDiff[Pair[1][0]] += 1

    # For plotting, this is the X axis list, and represents the index in the
    # output streams
    X = list(range(len(MinDiff)))

    # For each output index, count how many of the varied streams share the same
    # element value as the reference stream. 
    SameElementCount= len(Reference)*[0]   # create a zero list
    for i in range(len(Outputs)):
        for j in range(len(Reference)):
            if (Reference[j] == Outputs[i][j]):
                SameElementCount[j] += 1
        
    XS = list(range(len(SameElementCount)))

    # Create a new plot instance
    fig=plt.figure()

    # The first figure plots the number of output sequences that differ from the
    # reference as a function of the index of the first difference. For example, 
    # if x=10 and y=30, this means that there are 30 output streams out of 1431 that
    # are the exact same as the reference in elements 0-9; the 10th index is the
    # first at which they differ. 
    ax1=fig.add_subplot(2,1,1)
    plt.plot(X,MinDiff,"bo:")
    plt.xlabel("Index of first difference from reference")
    plt.ylabel("Count of output streams")
    plt.grid()

    # In the second figure, we look at how many of the output streams share the same
    # output card in the same position as the reference. This is not the first
    # index of difference like in the first plot. In this case, if x=10 and y=30, 
    # then 30 of the 1431 output streams have the same card in position 10 as the
    # reference stream. 
    ax2=fig.add_subplot(2,1,2)
    #plt.plot(X,Overlaps,"go:")
    plt.plot(XS,SameElementCount,"go:")
    plt.xlabel("Number of like elements in "+str(SampleSize))
    plt.ylabel("Count of output streams")
    plt.grid()
    plt.show()

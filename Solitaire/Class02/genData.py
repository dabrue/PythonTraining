#!/bin/env python3
"""
    This script generates a data set and writes it to a file. 
"""

__author__      = "Daniel A. Brue"
__email__       = "dabrue@us.ibm.com"


if (__name__ == "__main__"):
    
    # We'll use the math library for trig functions
    import math

    # First, lets construct some empty lists:
    x=[]
    y0=[]
    y1=[]
    y2=[]

    # Python also allows for multiple definitions per line, so we could do this...
    x, y0, y1, y2 = [], [], [], []

    # Set some data ranges on x, and number of points
    N = 101
    xmin = 0.0
    xmax = 10.0
    dx = (xmax - xmin)/(N-1)
    
    # Now populate the x array with floats
    for i in range(N):  # remmeber, range(10) provides 0-9
        x.append(i*dx)  # append a new value to the x list. 

    # Next, generate the y data by looping over the literable list x
    for ix in x:  
        y0.append(math.sin(0*ix))
        y1.append(math.sin(1*ix))
        y2.append(math.sin(2*ix))

    # For a sanity check, let's be sure that all of thse lists are the same length
    if ((len(x) != len(y0)) or (len(y0) != len(y1)) or (len(y1) != len(y2))):
        print("Length mismatch")


    # Now let's write these lists to a file in columns to be read in later
    # First we need a new file object. 
    OutputFileName = "simpledata.dat"
    
    # This line creates a new file object that is writable. 
    outf = open(OutputFileName,"w")  

    # File objects have a "write" method that only accepts strings. We need to convert
    # the data into a single string and add a newline character. 
    # Unlike the print() function, write() does not automatically append a newline. 

    sp="  "

    for i in range(N):
        # note that for strings, "+" concatenates
        line = str(x[i])+sp+str(y0[i])+sp+str(y1[i])+sp+str(y2[i])+"\n"
        
        # now write this line to our file,
        outf.write(line)

    # close the file. 
    outf.close()


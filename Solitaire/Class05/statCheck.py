#!/bin/env python3
"""
    This routine reads in the output of the Solitaire cipher algorithm and 
    runs some statistics on it. 
"""

__author__      = "Daniel A. Brue"
__email__       = "dabrue@us.ibm.com"

##########################################################################################
def CalcChi2(Observed, Expected):
    """
        This routine calculates the chi-squared test statistic
    """
    import math

    if (len(Observed) != len(Expected)):
        print("ERROR: CalcChi2, unequal lengths of Observed and Expected lists")
        exit(1)
    else:
        N = len(Observed)   # Number of observables
        df = N - 1 # define the degree of freedom

    X=[]
    for i in range(len(Observed)):
        x = (Observed[i]-Expected[i])**2 / Expected[i]
        X.append(x)

    chi2 = math.fsum(X)  # fsum performs "safe" summation, minimizes error

    return chi2, df
    


##########################################################################################
if (__name__ == "__main__"):
    import sys
    import argparse
    import numpy
    import scipy.stats
    import math
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import re


    parser = argparse.ArgumentParser(description="Solitaire Statistics")
    parser.add_argument("-i","--input",dest="infileName",action="store",
        default=None,help="Input file name")
    parser.add_argument("--makeplots",dest="makeplots",action="store_true",
        default=False,help="flag to make plots")

    args=parser.parse_args()

    mkplts = args.makeplots

    # Read in observables and count them
    with open(args.infileName,"r") as f:
        lines = f.readlines()

    Mode=None
    s=[]  # Singles count array
    d=[]  # Doubles count array
    t=[]  # Triples count array
    for line in lines:
        line=line.rstrip("\n")
        if (re.match("# SINGLES",line)):
            Mode="SINGLES"
            data=line.split()
            N = int(data[2])
            singles = numpy.zeros(N,dtype=numpy.int)
            continue  # cycles the loop
        if (re.match("# DOUBLES",line)):
            Mode = "DOUBLES"
            doubles = numpy.zeros([N,N],dtype=numpy.int)
            continue
        if (re.match("# TRIPLES",line)):
            Mode = "TRIPLES"
            triples = numpy.zeros([N,N,N],dtype=numpy.int)
            continue
        if (re.match("\s*$",line)):
            # skip blank lines
            Mode = None
            continue

        if (Mode == "SINGLES"):
            data = line.split()
            i = int(data[0])
            c = int(data[1])
            singles[i] = c
            s.append(c)
        elif (Mode == "DOUBLES"):
            data = line.split()
            i = int(data[0])
            j = int(data[1])
            c = int(data[2])
            doubles[i][j] = c
            d.append(c)
        elif (Mode == "TRIPLES"):
            data=line.split()
            i = int(data[0])
            j = int(data[1])
            k = int(data[2])
            c = int(data[3])
            triples[i][j][k] = c
            t.append(c)
            
            
    ######################################################################################
    # SINGLETS: run stats on single characters observations in this section


    TotalObservations = sum(singles)
    print("Total number of observations is "+str(TotalObservations)+"\n")

    # Generate a zero-filled array that is the same shape and type as Observed
    Frequency = numpy.zeros_like(singles) 
    # Unfortunately, this fails for frequency, since it is defined as an integer
    # type, trying to assign values on [0,1] always gives zero. So we redefine it
    # as a float data type
    Frequency = numpy.zeros(N,dtype=float)
    
    for i in range(N):
        Frequency[i] = singles[i]/TotalObservations

    if (mkplts):  # make a plot to show the data
        x=list(range(N))
        fig=plt.figure()
        ax1=fig.add_subplot(2,1,1)
        plt.plot(x,singles,"bo:")
        plt.ylabel("Observation Count")
        plt.xticks(x,[]) # No x tick labels
        ax2=fig.add_subplot(2,1,2)
        plt.plot(x,Frequency,"ro:")
        plt.ylabel("Frequency")
        plt.show()
        

    # Now we establish the "Null Hypothesis". If Solitaire is a good random
    # number generator, then it should have totally uniform output. 
    Expected = numpy.zeros(N,dtype=float)
    for i in range(N):
        Expected[i] = TotalObservations/N

    # Determine the chi-squared test statistic assuming that the null hypothesis
    # is a perfectly uniform distribution
    chi2,df = CalcChi2(singles,Expected)
    print("Singlet Chi2 value is "+str(chi2))


    # Next we create a chi2 stat object from the scipy library
    # ref: http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2.html#scipy.stats.chi2
    chi2dist = scipy.stats.chi2(df) # takes the number of degrees of freedom as argument

    # the chi2dist object provides access to the distributions associated with the
    # chi-squared test statistic for this number of degrees of freedom. 
    if (mkplts):
        # Generate a uniform list of floats with linspace
        x=numpy.linspace(0,4*df,1001)
        pdf = numpy.zeros_like(x)  # Probability distribution
        cdf = numpy.zeros_like(x)  # Cumulative distribution
        sf  = numpy.zeros_like(x)  # Survival Function (1-CDF)
        for i in range(len(x)):
            pdf[i] = chi2dist.pdf(x[i])
            cdf[i] = chi2dist.cdf(x[i])
            sf[i] =  chi2dist.sf(x[i])
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        plt.plot(x,pdf,"k-",label="PDF")
        plt.plot(x,cdf,"b-",label="CDF")
        plt.plot(x,sf,"r-",label="SF")
        plt.legend(loc=7)
        plt.show()

    Probability = chi2dist.sf(chi2)
    Percent = Probability*100
    strPercent = "{:3.2f}".format(Percent)
    print("Assuming the Null Hypothesis is True, the probability of observing a")
    print("distribution at least this extreme is "+strPercent)
    print("\n")
    

    ######################################################################################
    # DOUBLES
    
    df = len(singles)**2 - 1

    # We reduce TotalObservations by 1 because there is one fewer digraph count than
    # single character count
    TotalObservations = math.fsum(singles) - 1

    Expected=numpy.zeros(len(d),dtype=numpy.float)
    Expected = Expected + TotalObservations*1.0/(df+1)
    print(Expected[0])
    chi2,df = CalcChi2(d,Expected)
    print("Doubles chi-squred is "+str(chi2))
    chi2dist=scipy.stats.chi2(df)
    Probability=chi2dist.sf(chi2)
    Percent=Probability*100
    strPercent = "{:3.2f}".format(Percent)
    print("Assuming the Null Hypothesis is True, the probability of observing a")
    print("distribution at least this extreme is "+strPercent)
    print("\n")

    if (mkplts):
        x = list(range(len(d)))
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        plt.plot(x,d,"bo-")
        plt.show()

        # make a more helpful bar plot
        Nlines = len(doubles)
        x=list(range(Nlines))
        Colors = Nlines*["r","y","g","c","b","m"]
        Colors = list(Colors[:Nlines])
        Z=list(range(Nlines))
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1,projection="3d")
        k=-1
        for color, z in zip(Colors,Z):
            k+=1
            xs = list(x)
            ys = list(doubles[k])
            #ax.bar(xs, ys, zs=z, zdir='y', color=color, alpha=0.8)
            ax.bar(xs, ys, zs=z, zdir='y', color=color, alpha=1.0)
        plt.show()

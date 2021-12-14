#!/usr/bin/env python3
"""
    Analyze probabilities of repeat events

    Also, Numerically show convergence of Geometric Series

    A geometric series is one that follows
    S = a + ar + ar^2 + ar^3 + ar^4 .....

    The sum of N terms of a Geometric Series is given by 

    S(N) = a(1-r^N)/(1-r)

    if abs(r) < 1.0 , this series converges asymptotically to 
    
    S(infty) = a/(1-r)

    In the present case of probabilities, we want a = p and r = q = 1-p.
    Given this, the asymptotic sum is 1. 

    Derivation is simple:
    S = a + ar + ar^2 + ar^3 + ar^4 ...
    rS = ar +ar^2 + ar^3 + ar^4 + ar^5 ...
    S-rS = a 
    S = a / (1-r)  (iff abs(r) < 1 and S is infinite)
"""

__author__ = "Daniel Brue"
__email__  = "dabrue@gmail.com"

import random

random.seed()

def roll_die(Number_Of_Sides=6):
    return random.randint(1,Number_Of_Sides+1)


if (__name__ == "__main__"):
    import argparse
    import re
    import math
    import numpy
    import scipy
    import matplotlib.pyplot as plt
    import sys
    import random

    # Set up the argument parser with commands
    parser = argparse.ArgumentParser(description = "dice parms")
    parser.add_argument("--sample-size",dest="SampleSize",type=str, action="store",
        default="10K",help="The sample size")
    parser.add_argument("--sides",dest="Number_Of_Sides",type=int,action="store",
        default=6,help="Number of sides on the die")
    parser.add_argument("--foo",action="store_true")
    args=parser.parse_args(sys.argv[1:])

    SampleSize =args.SampleSize
    NSides = args.Number_Of_Sides

    # Turn sample size into an integer
    a=re.match("(\d+)([KMBGT]*)",SampleSize)
    fac=1
    if (len(a.group(2)) == 1):
        if (a.group(2) == "K"):
            fac=1000
        elif (a.group(2) == "M"):
            fac=1000000
        elif (a.group(2) == "B" or a.group(2)== "G"):
            fac=1000000000
    SampleSize=int(a.group(1))*fac

    print("Sample Size = ",SampleSize)

    # Build variables for theoretical expectations
    p = 1.0/NSides
    q = 1.0-p

    # Build an array to track repeated events
    distances=[]
    sides=[]
    for i in range(1,NSides+1):
        sides.append((i,0))
    marker=dict(sides)
    i=0
    count=0
    while (i < SampleSize):
        count+=1
        k = random.randint(1,NSides)
        if (marker[k] != 0):
            distance=count-marker[k]
            distances.append(distance)
            i+=1
        marker[k]=count


    largest_distance = max(distances)
    x=range(largest_distance+2)
    maxx=max(x)
    y=[]
    for i in range(len(x)):
        y.append(0)
    for i in range(len(distances)):
        y[distances[i]] += 1

    ycom=[]
    for i in range(len(y)):
        y[i] = y[i]/SampleSize
        ycom.append(y[i]*i)

    # Get the analytic line
    xanal = numpy.linspace(1,maxx,10001)
    yanal = numpy.zeros_like(xanal)
    lnq=math.log(q)
    for i in range(len(xanal)):
        yanal[i] = p*math.exp((xanal[i]-1.0)*lnq)

    # Get cumulatives
    cy = numpy.zeros_like(y)
    com = numpy.zeros_like(y)
    for i in range(len(y)):
        j=i+1
        cy[i] = p*(1.0-q**i)/(1.0-q)
        com[i] = math.fsum(ycom[:j])
    


    fig=plt.figure()
    ax0=fig.add_subplot(2,1,1)
    plt.plot(xanal,yanal,"r-")
    plt.plot(x,y,"bo")
    plt.ylabel("Probability")
    plt.xlabel("Roll Number")

    ax1=fig.add_subplot(2,1,2)
    plt.plot(x,cy,"bo")
    plt.plot(x,com,"go")
    plt.show()

    print(x[0],y[0],ycom[0])

    # We can show analytically that the mean of the distribution is NSides. Next, let's 
    # calculate the variance. As far as I can tell for right now, this must be done
    # numerically, not analytically. At least, for the discrete version. It should be
    # provable from the continuous version. 

    i=1
    mean_terms=[p]
    variance_terms=[p]
    prob_terms=[p]
    mu=[]
    SS=[]
    while (i < 10**6):
        probi=p*(q**i)
        s=i*probi
        t=i*s
        prob_terms.append(probi)
        mean_terms.append(s)
        variance_terms.append(t)
        if (t < 1.0e-30):
            break
        i+=1
    P=math.fsum(prob_terms)
    mu=math.fsum(mean_terms)
    SS=math.fsum(variance_terms)
    #print(mu,SS,len(mean_terms))
    print(P)
    print(mu)
    print(SS)
    print(len(prob_terms))

    ss = 1.0/p + 2*(p-p**2)/(p**3)
    print(ss)
    expectation = NSides
    variance = NSides**2-NSides
    standard_deviation = math.sqrt(variance)
    print("expectation value  = "+str(expectation))
    print("variance           = "+str(variance))
    print("standard deviation = "+str(standard_deviation))

    print("\n")

    

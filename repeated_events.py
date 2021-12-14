#!/usr/bin/env python3
"""
    Analyze probabilities of repeat events

    D. A. Brue 2013
"""

import random

random.seed()

def roll_die(Number_Of_Sides=6):
    return random.randint(1,Number_Of_Sides+1)


if (__name__ == "__main__"):
    import argparse
    import re
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
    y=[]
    for i in range(len(x)):
        y.append(0)
    for i in range(len(distances)):
        y[distances[i]] += 1

    for i in range(len(y)):
        y[i] = y[i]/SampleSize

    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    plt.plot(x,y,"bo")
    plt.show()

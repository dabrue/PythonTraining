#!/usr/bin/python

import matplotlib
import numpy
import scipy
import math

# Define the spatial spectrum [x:-1,1]
def Oxy(x):
    if (math.fabs(x) > 1.0):
        print "Error, Oxy out of bounds, x=", x

    # Now define function, go 1D 
    if (math.fabs(x) <= 0.5):
        O = 1.0
    else: 
        O = 0.0

    return O



# Test the spatial function
x=numpy.linspace(-1.0,1.0,31)
O=[]
for i in range(len(x)):
    O.append(Oxy(x[i]))

print O



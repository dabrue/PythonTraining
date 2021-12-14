#!/usr/bin/env python3
"""
    Numerically show convergence of Geometric Series

    A geometric series is one that follows
    a + ar + ar^2 + ar^3 + ar^4 .....

    The sum of N terms of a Geometric Series is given by 

    S(N) = a(1-r^N)/(1-r)

    if abs(r) < 1.0 , this series converges asymptotically to 
    
    S(infty) = a/(1-r)

    In the present case of probabilities, we want a = p and r = q = 1-p.
    Given this, the asymptotic sum is 1. 
"""

import math
import mathplotlib.pyplot as plt


N = 1000
p = 0.1
q = 1.0-p

Prob = N*[0]
Cumu = N*[0]
Derv = N*[0]

for i in range(N):
    Prob[i] = p*q**i
    Cumu=math.fsum(Prob)

k = math.fsum(Prob)
print(N,k)



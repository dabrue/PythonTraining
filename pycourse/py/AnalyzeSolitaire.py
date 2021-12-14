#!/bin/env python3
"""
    Analysis script for Solitaire Algorithm

    Tests to Perform:
    1. Frequency count of output letters
    2. Frequency count of output numbers
    3. Changes in statistics based on output length
    4. Chi-Squared comparision to perfect randomness
    5. Entropy content of output algorithm per character
    6. Length of similar output per card variance in key
    
"""

__author__   = "Daniel Alan Brue"
__email__    = "danielbrue@gmail.com"
__PGPKeyID__ = "2DFDF230"
__status__   = "Development"
__copyright__= "None"
__version__  = "0.5"


import numpy
import math
import scipy
import matplotlib.pyplot as plt
import matplotlib
import re
import Solitaire

# Set matplotlib to use latex for plot labels
matplotlib.re("text",usetex=True)



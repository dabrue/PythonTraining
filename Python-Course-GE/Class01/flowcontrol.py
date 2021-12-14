#!/bin/env python3
'''
    Examples of flow control. Not fluids.

    This is also where Python's formatting becomes important
'''

__author__ = 'Daniel Brue, danielbrue@gmail.com'
__PGPID__  = 'DF27 C041 7453 8168 82B9  5319 32F0 4518 4B36 16AD'

# Logistics.  'True' is a built in name in Python, as is 'False'
true = True
false = False  

# Python is whitespace aware. Most modern programming languages are not this way
# but rather than have 'end' statments for logic or flow blocks, Python handles
# this with indentation. 
#
# An indent is required after a conditional or loop block, as so...

if (true):
    print("It's True!")
elif (true and false):
    print("This is not true")
elif (True or False):
    print("'and', 'or', 'not', are all Python control words")
else:
    print("we're really never going to get here ever")


# It does not matter how much white space is used for indentation, but there must
# be some. Instead of an end statement, the conditional block finishes when the
# next line appears without indentation. 

a = 5  # this line defines a, and closes the 'else' part of the 'if' block. 

# Python will complain if it doesn't understand the whitespace structure. 

if (true):
    a=5
elif (true):
  b=4  # This used to not be OK, but apparently now it is. 
else:
    x=1

# Note how above, the two lines in the clauses of the conditional are not indented
# the same. This will confuse Python. A logical block must have all the same indentation
# but it does not have to be the same for the whole script, e.g....

if (true):
 a=5
else:
 b=4


# Loops are controled by 'iterables'. An 'iterable' describes something that, well, 
# can be iterated upon. This may be a list, a dictionary's keys, a set, a tuple, or
# a 'generator'. 

# A list is an iterable, so a simple loop might look like
for i in [1, 2, 3, 4, 5]:
    print(i)

# but a more common method would be to use the built-in range() function
for i in range(1,6):
    print(i)

# here range is a "generator". It is an object that when called repeatedly produces
# a sequence that can be iterated. range() takes at least one argument, 
#
# range(6) will produce integers 0-5 
# range(1,6) will produce integers 1-5
# range(10,4,-1) will produce integers 10, 9, 8, 7, 6, 5, but not 4

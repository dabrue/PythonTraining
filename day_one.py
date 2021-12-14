#!/usr/bin/env python3
""" This is an introductory script for Python

    This is a doc string, and while it is ignored in code, it is recognized
    by Python as different from standard comments. 

    All python routines have the ability to contain documentation strings. 
    Unlike comments, these are meant to aid access and usability of the code, 
    not to explain the code itself. 

    The doc strings for any python routine can be called forth as a string
    object by the calling routine. This makes doc strings accessible at runtime.
"""

# This is a standard comment, and is not accessible at runtime. 


# Note that Python employs automatic type casting. No declarations of variables
# or types is necessary. 
a=1

print(a)  # print() is a Py3 convention. In Py2, it's just "print a"

# The built-in type() function returns the type of variable. 
print(type(a))

a="IBM"
print(a,type(a))


# Note that the print function automatically appends a newline character, "\n", 
# whereas a write statement does not. 



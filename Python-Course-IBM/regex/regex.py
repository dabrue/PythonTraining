#!/bin/env python3
"""
    Regular Expressions In Python

    Contents:
    0 - Python's re module
    1 - General Regex: Special Characters
"""

__author__      = "Daniel A. Brue"
__email__       = "dabrue@us.ibm.com"

##########################################################################################
# Constants for formatted output
sbar = 90*"-"
dbar = 90*"="

##########################################################################################
def lineno():
    """
        Returns the current line number
    """
    # The inspect module can get information about this script into the script
    import inspect
    return inspect.currentframe().f_back.f_lineno



##########################################################################################
def re_Module(text=None):
    """ 
        An introduction to invoking the re module commands
    """
    import re

    print(dbar)
    print("re Module Examples")

    pass


##########################################################################################
def Regex_SpecialCharacters(text=None):
    """
        General Regex, Special Characters: 
        The backslash is important!

        ^   - NOT and beginning of string, depending on context
        \A  - beginning of the string
        \Z  - end of the string
        $   - end of string  (even if containing \n newline). If the string 
              ends with a newline, the $ matches right before it. 
        \$  - literal dollar sign
        \s  - White Space  (space, newline, return, tab)
        \S  - NOT white space
        \b  - word boundary e.g. \bword\b
        \d    - matches any digit
        [0-9] - matches any digit
        [a-z] - matches any lower case letter
        [A-Z] - matches any upper case letter
        \w  - word character e.g. a-z, A-Z, 0-9 and underscore
        \W  - NOT word character
        \t  - tab
    """
    import re
    print(dbar)
    print("Special Characters in Regular Expressesion")

    pass

if (__name__ == "__main__"):

    # A single backslash in python is recognized as a line continuation. 
    # No characters can follow (including white space or comment)

    here=lineno()
    print("Sample Text defined on Line "+str(here+2))
    text=\
    "Archimedes stepped into the public bath and noticed the water, displaced by\n"\
    "his bulk, slosh over the side. \"Eureka! Eureka!\", he yelled as he ran naked\n"\
    "through the streets of Syracuse. \"I\'ve found it! I\'ve found it!"
    # Note that the quote required backslashing the quotation marks so that they
    # are interpreted as literals and not as the end of the string. 

    print("Original Text:")
    print(text)
    

    """
        Character class subtraction:
        [a-z-[aeiou]] finds all non-vowel letters
    """

    "[^A-Z]"  # Not A-Z

    returnCode = re_Module(text)

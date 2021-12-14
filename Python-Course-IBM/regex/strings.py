#!/bin/env python3
# -*- coding: UTF-8 -*-
"""
    Demonstrations of Strings in Pythoin
"""

__author__      = "Daniel A. Brue"
__email__       = "dabrue@us.ibm.com"

"""
    Encoding: 

    By default, Python expects ASCII encoding. However, the source code encoding can be 
    changed by including a 'magic' comment on the first or second line of the source code
    that defines the encoding. This defines the encoding that the Python parser will use
    for the source. 
"""

# String literals have the form
# [stringprefix](shortstring | longstring)

"""
    String Prefix:

    The string prefix can be one of 'r', 'u', 'R', 'U' where r or R are used
    to indicate raw strings and u or U are used to indicate unicode strings. 

"""

# Two or more string literals next to each other are automatically concatenated
# These must be 'hard coded' literals, it does not work with variables, e.g.
Python = "Py" "thon"  # auto concatenates
Version = Python+"3"   # Does not autoconcatenate, "+" is required 

# Note the string prefix "r" at the beginning of this doc string. This allows for
# ignoring the escaped characters in the string, so \t will literally show "\t" and
# not a tab. 
r"""
    Python recognizes escaped (backslashed) characters similar to Standard C
    
    \newline    Backslash and newline ignored    
    \\  Backslash (\)    
    \'  Single quote (')     
    \"  Double quote (")     
    \a  ASCII Bell (BEL)     
    \b  ASCII Backspace (BS)     
    \f  ASCII Formfeed (FF)      
    \n  ASCII Linefeed (LF)      
    \r  ASCII Carriage Return (CR)   
    \t  ASCII Horizontal Tab (TAB)   
    \v  ASCII Vertical Tab (VT)      
    \ooo    Character with octal value ooo  (1,3)
    \xhh    Character with hex value hh     (2,3)

"""



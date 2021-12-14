#!/bin/env python3

# This is a comment. Comments are ignored by Python, and begin with a # symbol. 
#
# The first line above is special. On Windows, it is recognized as a comment
# but in Linux/Unix environments, it is called a "shebang", noted with the leading
#   "#!" combination. This tells the computer what execuatable to use to interpret the
# following script. 
#
# In Linux/Unix, the shebang is followed by a path to an executable, such as python, 
# perl, bash, zsh, etc. In the case above, I have called the "env" executable, which
# is a program that will return the path to python3, which can be useful on Linux systems
# when the script may need be be run on different computers with different paths to the
# python interpreter. 
#
# In Windows, the shebang line is ignored, and the interpreter for the script is chosen
# by Windows' file associations. So, if set up correctly, a .py file extension will tell
# Windows which python interpreter to use to execute the script. 

# These following lines become attributes of this script. The double underscores are not
# necessary, but by convention distinguish these variables from vars used in code. 
__author__ = 'Daniel Brue, danielbrue@gmail.com'
__PGPID__ = 'DF27 C041 7453 8168 82B9  5319 32F0 4518 4B36 16AD'

'''
This is a documentation string, or docstring. 

Docstrings are text in a python script that are preceeded and followed by either
triple single quotes or triple double quotes. Use whichever you prefer. 

Doc strings are different from comments in that they can be extracted by Python
during run time. Therefore, they can be used to document the code both when looking
at the source, and as a way to convey information if desired when the code is run. 

Every module or library created should have a docstring. 
'''

##########################################################################################
# DATA TYPES AND OPERATIONS
##########################################################################################

a = 5  # defining a to be an integer
print(a)
print(type(a))  # 'type' is built-in, and returns what class the argument is

b = 9

# add
c1 = a + b
# subtract
c2 = a - b
# multiply
c3 = a * b
# divide
c4 = a / b

# in the last case, python automatically type converted c4 to 'float'
print(c1,c2,c3,c4)
print(type(c1),type(c2),type(c3),type(c4))

# exponentiation
c = a ** b
print(a, '**', b, ' = ',c)  # the print command can take multiple arguments

# Now, you *can* do multiple assignments in one line, such as, 
a, b = 2, 3
# This is not uncommon to see. In my personal opinion, I would prefer to not do this, as
# it makes the code more cumbersome to read and is not computationally any more efficient
# than, 
a = 2
b = 3


#-----------------------------------------------------------------------------------------
# LOGIC
# Python recognizes built-in logics of True and False
true = True  # variable = boolean True
false = False # 





#-----------------------------------------------------------------------------------------
# Strings Next!
s = 'This is a string. Single or double quotes are OK'
print(s)
print(type(s))
print(len(s))
print(s[6])

# Note that python begins indices at 0, not at 1, so the sixth index is 's'

# On to sequences of data!

#-----------------------------------------------------------------------------------------
# LISTS
l = [1, 2, 3, 4, 5, 6]  # this is a list, denoted with square brackets

# like strings, lists have indices and lengths
print('l=',l)
print('len(l) = ',len(l))
print('l[0] = ', l[0])

# A list can be a list of ANYTHING
l2 = ['a', 3, s, 4.56]
print(l2)
# even a list of lists....
l3 = ['a', l2, s]
print(l3)


#-----------------------------------------------------------------------------------------
# TUPLES
# A tuple is similar to a list, 
t = ( 1, 2, 3)
print(t)
print(type(t))
# but it has a distinct difference
#   a tuple is immutable. Once created, it cannot be changed. This is useful sometimes
#   for dealing with data that you don't want to alter or that must maintain a consistent
#   hash value. To change it, it must be recreated. The individual elements of a tuple
#   are accessible, just like a list, but they cannot be assigned or changed. 
print(t[1])
# t[2]=a   # <- this will throw an error

#-----------------------------------------------------------------------------------------
# SETS
# A set is also like a list, but must contain all the same type of elements, and only 
# one of each. Where a list may have repeating elements, a set can not. 
s = { 1, 2, 3, 4, 5}
print('set s=',s)

# but if I try to add duplicates, it the set will automatically remove them. 
s = {1, 1, 3, 4, 5}
print('set s=',s)

# Sometimes this is useful, if, for instance, we wanted to see how many duplicate
# elements there are in a list, we could do this...
l = [1, 2, 3, 3, 4, 4, 6, 7, 7, 7, 9]
s = set(l)  # the set command changes the data type to a set
print((len(l)-len(s)),' duplicates in the list')


#-----------------------------------------------------------------------------------------
# DICTIONARIES
# Dictionaries are incredibly useful. Unlike lists or tuples, their elements are not 
# referenced by index, but by a 'key' value. For this reason, they also do not maintain
# a set order
D = {'a':1,2:'b','c':'dog'}
print(D['a'],D[2],D['c'])

# There are a few important things to note about dictionaries. Their order is not 
# set in stone, and they cannot be indexed in sequence, but only by reference. 
# To see the references, we use the .keys() function of the dictionary object...
print(D.keys())
# However, this is not an independent object in itself, but a "view" of the dictionary
# object. If you want a list of the keys of a dictionary, you must use the list command
DList = list(D.keys())
# This changes teh data type of the keys to be members of the list DList. 


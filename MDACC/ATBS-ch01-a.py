#!/usr/bin/env python3
'''
Following Chapter 1 of "Automate The Boring Stuff" python programming book.

A few notes to start out: 

    1. WHAT IS PYTHON? 
    Python is an interpreted programming language. This is different than compiled
    programming languages, such as C or Fortran, etc. The key difference is in what
    code is running on your computer. 

    In compiled languages, source code (say, in C) is "compiled", which means that
    a different program (a compiler) will read in the source code and convert it into
    something that the computer can understand as a set of instructions. There are
    many compilers for many languages. The most common are the GNU set of compilers
    because they are freely available and therefore ubiquitous. However, some 
    companies make specialized compilers. For example, Intel makes and sells their own 
    compilers with the understanding that programs compiled with Intel compilers will
    run better on Intel's chips. 

    The really important thing to remember about compiled programs is that they only
    run on the machines they were compiled for! A program written in C and using
    a compiler for an x86 architecture on Windows will NOT run on a computer running
    Linux on the IBM Power architecture. These different operating systems and different
    chipsets will require different sets of instructions. 

    An "interpreted" programming language is different. It can be thought of as 
    "compiled-on-the-fly". The text of the source code (like this file itself) is read
    by the interpreter (python3 in this case, which is what line 1 means above! We 
    will come back to that in a bit). The interpreter than constructs the set of
    computer instructions and runs them. In this way, it is similar to compiled code
    if the "compile" and "run" steps were combined. The major benefit, however, is that
    the "program" written in Python can be shared with any machine of any OS and any
    architecture that has a Python interpreter. Code I write in Linux can run on 
    Windows without any problem, but a code compiled for Linux cannot run on Windows. 

    2. SIGNIFICANT DIFFERENCES between compiled and interpreted

    It should be noted that for small programs, compiling is fast, but for larger
    ones it can take a very significant amount of time. Hours isn't unheard of. 

    Interpreted languages also have another huge advantage. It is the Python interpreter
    that understands what OS it is running on, not the code itself. What this means is
    that if I write a python script that makes plots, I do not have to worry about 
    using the correct display drivers for Windows or Mac or Linux, the interpreter
    does that for me. This means that I can write Python code that runs on all of these, 
    whereas for C code, the source code must be changed depending on what OS and Arch
    that it is written for. 

    For these reasons, Python has become a very, very popular language for collaborations
    and for research purposes. It is much easier to share code and have it run reliably on
    many different platforms. 


    3. DOC STRINGS and COMMENTS 
    This text written right here is a "doc string", and is denoted in the Python 
    launguage as anything within a triplet of quotation marks. Either three ' symbols
    or three " symbols. 

    Doc strings are different than comments. A comment in Python is anything following
    a # symbol. It can be an entire line, or it can be an in-line comment. 

    for example...

    # This entire line would be commented

    whereas

    c = a + b  # the calculation is performed, and the rest of the line is a comment

    The difference between docstrings and comments is that comments are completely
    ignored by the interpreter; they do not become part of what runs on the computer
    at all. 

    Doc Strings on the other hand ARE read by the interpreter, and saved as part of
    the code that is being run. Doc strings are able to be printed and are accessible
    to the code itself. In this way, consider doc strings to be part of the code itself,
    whereas comment statements are not part of the code at all. 

    This can be a very useful thing! Python is able to collect doc strings to make
    a separate documentation (e.g. pdf, html, etc.) about the code! They should be used
    for describing what the code is supposed to do, what it needs, etc. Comments, 
    on the other hand, are useful for describing what certain parts of the code are doing. 
    For instance, if we write a very complex mathematical formula, it is helpful to 
    add comments that explains it to anyone reading the code. 

    Rule of thumb: Doc Strings are intended to provide information to people running
    the code. Comments are intended to provide information to people reading the code. 

    This next line of a triplet single quotes will close this doc string.
    '''

# This comment line will be ignored, the next line is code:
print("This print statement is the first line of code")

# Python has several built-in data types. These can be set implicitly or explicity. 
# For example, 

a = 5

# The above line sets 'a' as having a value of 5. Actually, what happens behind the scenes
# is that the number 5 is given the name 'a', but let's not worry about that right now. 

# We can print this as
print('a = ', a)

# Note that 'print' is a function that can take any number of arguments and simply
# writes their values to the screen. In the above line, we are printing a string 'a = '
# and then the value of 'a'. These two arguments are separated by a comma. 

# Now, we set a=5, and implicitly, Python will consider 'a' to be an integer. We can see 
# this using the built-in type() function. 

print('a = ',a, ' type(a) = ', type(a))

# Both 'print' and 'type' are built-in functions recognized by Python. There are many of
# these, and the best source to learn about them is Python's official documentation at
# https://docs.python.org

# Let's do the same thing again, but with real numbers
b = 5.0
print('b = ', b)
print('b = ',b , ' type(b) = ', type(b))

# This will tell you that b is of type 'float', which is the term used for numbers that
# have fractional components. Even though in this example, 'a' and 'b' both equal 5, 
# they DO technically equal different values of 5! 

# There are very good reasons for why we differentiate these data types. If we are
# working with only integers, then we can actually write faster and more efficient code
# if we let the computer know that it never has to worry about finding decimal places
# or exponents. 

# It should be noted, that a mathematical operation that involves an integer and a float
# will typically convert the end result to a float. For instance: 

c = a + b
print('c = a + b   where')
print('a = ',a,' type(a) = ', type(a))
print('b = ',b,' type(b) = ', type(b))
print('c = ',c,' type(c) = ', type(c))

# We see that int + float = float. Same with subtraction, mult, div, etc.

# The book goes through the various arithmetic operators (+*-/ etc). However, there is
# one other VERY IMPORTANT TRICKY THING TO REMEMBER! These operators may mean different
# things based on what data types we're using! The jargon term for this is "overloaded"
# operators. the "+" symbol means something different for integers than it does for strings. 

# note that adding in '\n' to the string being printed will create a new line. This is 
# called a control character, or an 'escape' character, and Python recognizes it as special
# because of the leading backslash. There are many control characters in strings. 

print('\nNOW WE LOOK AT STRING OPERATORS\n')

# (quick aside note, it does not matter if strings use single or double quotes, but 
# note that whatever you open with you must close with. 

string1 = "This is our first string"
string2 = " violinist of our philphythonic orchestra"
string3 = string1 + string2
print('string 1 = ', string1)
print('string 2 = ', string2)
print('string 3 = ', string3)

# !!!!
# Note that with strings, the '+' operator concatenates strings, whereas for int or float
# the '+' operator performs addition


'''
This final doc string is to say that 100-300 lines per file is typical of code. More than
that can be awkward to follow, and it makes no difference whether code is in multiple
files or in a single monolith. We will see later how to access code in different files. 
For now, we'll quit this file and start a new one to continue on data types.
'''




#!/bin/env python3
"""
    Driver routine for using the Solitaire encryption algorithm
    
    Python class 4
"""

__author__      = "Daniel A. Brue"
__email__       = "dabrue@us.ibm.com"

if (__name__ == "__main__"):

    # Solitaire is the code we wrote for class 3 that contains the cipher implementation
    import Solitaire
    # the sys module provides system-specifc information and commands. We will use it
    # to access the command line arguments passed to this python code
    import sys

    # argparse is a module to interpret command line arguments
    import argparse

    # os.path provides commands to query the file system. 
    import os.path

    #####################################################################################
    # Define some useful constants
    YES = ["y","Y","yes","Yes","YES"]
    NO  = ["n","N","no","No","NO"]
    

    #####################################################################################
    # ARGPARSE command line options parsing. This section sets up the argparse 
    # object that will be used to interpret the command line arguments. 

    # Creat a new parser object with a description of the program
    parser = argparse.ArgumentParser(description="Encrypt/Decrypt with Solitaire")

    # Next we add the list of expected arguments
    parser.add_argument("-i","--input",nargs=1,dest="inputName",action="store",
        default=[],help="Input file name")
    parser.add_argument("-o","--output",nargs=1,dest="outputName",action="store",
        default=[],help="Output file name")
    parser.add_argument("-k","--key",nargs=1,dest="key",action="store",
        default="",help="Encrypt/Decrypt key. This can be a file or it can\
               be a string at the command line")

    # We want to know what operation mode we are in. This is a set of mutually
    # exclusive options, so we group them. One and only one of these options
    # MUST be present
    modegroup = parser.add_mutually_exclusive_group(required=True)
    modegroup.add_argument("-e","--encrypt",dest="ENCRYPT",action="store_true",
        default=False,help="Use Encrypt mode")
    modegroup.add_argument("-d","--decrypt",dest="DECRYPT",action="store_true",
        default=False,help="Use Decrypt mode")
    modegroup.add_argument("-O","--output-only",dest="OUTPUT",nargs=1,action="store",
        default=False,help="takes int argument, provides that number of output chars")

    # extraneous options
    parser.add_argument("-5","--fives",dest="fives",action="store_true",
        default=False,help="Produce output in blocks of 5 chars, 10 blocks to a line")

    #####################################################################################
    # Now we give our constructed parser the list of command line arguments from
    # sys.argv which is a list. The zeroth element of the list is the calling python
    # program, so we only want the elements in the [1:] slice of sys.argv
    args=parser.parse_args(sys.argv[1:])

    # This new parser object, args, has attributes that correspond to our parser
    # object's "add_argument" calls. For instance, args.ENCRYPT will be True if
    # the "-e" flag was given at the command line. 
    
    #####################################################################################
    # the next step is to take action based on what the command line arguments were

    # NOTE: Because we used the "nargs" flag in the input and output command line
    # options in argparse, the inputName and outputName constructs are lists, not
    # strings. With nargs=1, they are single item lists. 

    # The following lines differ from what we did in class: the call to 
    # os.path.isfile for the input file has been replaced with a try-except block


    if (args.ENCRYPT or args.DECRYPT):
        try:
            with open(args.inputName[0],"r") as f:
                inputAll=f.read()
        except:
            sys.stderr.write("ERROR: problem reading input file\n")
            raise
    else:
        # Assuming in output-only mode. 
        pass

    # Now handle output file. If a file name is given, use it, else write to screen
    if (len(args.outputName) > 0):
        # check if the output file already exists and query for action if it does. 
        if (os.path.isfile(args.outputName[0])):
            sys.stdout.write("Output file "+args.outputName[0]+" exits. Overwrite?\n")
            YN=input("[y/N] ")

            # YES is a list defined early in this script. This if simply checks if 
            # the provided response is in the list of responses that mean "yes"
            if (YN in YES):
                outf=open(args.outputName[0],"w")
            else:
                sys.stderr.write("Unrecognized response\n")
                exit(0)
        else:
            # file doesn't exist, open it
            outf=open(args.outputName[0],"w")

    else:
        outf = sys.stdout   # make output standard out
            
    #####################################################################################
    # Get the key 
    if (os.path.isfile(args.key[0])):
        with open(args.key[0],"r") as f:
            keylines = f.read()
        key = Solitaire.sanitizeText(keylines)
    else:
        key = Solitaire.sanitizeText(args.key[0])
    #####################################################################################
    # Initialize a cipher instance and key the cipher
    Cipher = Solitaire.SolitaireCipher()

    Cipher.keyDeck(key)
    

    #####################################################################################
    # Clean input and perform encrypt/decrypt/output operation


    if (args.ENCRYPT):
        cleanInput = Solitaire.sanitizeText(inputAll)
        print("ENCRYPTING")
        outputString = Cipher.encrypt(cleanInput)
    elif (args.DECRYPT):
        cleanInput = Solitaire.sanitizeText(inputAll)
        print("DECRYPTING")
        outputString = Cipher.decrypt(cleanInput)
    elif (args.OUTPUT):
        try:
            Nout = int(args.OUTPUT[0])
        except:
            sys.stderr.write("Problem determining number of output chars")
            raise  # show the exception to stderr and exit. 
            # NOTE: you can raise an exception of your chosing by using
            # the raise command. With no specific exception given here, 
            # it implicitly uses the exception raised from the
            # failure to convert args.OUTPUT[0] to an integer. 
            
        outputList = Cipher.outputOnly(Nout,skipJokers=True,AZRange=1)
        outputString = Solitaire.numbersToText(outputList)

    if (args.fives):
        outputFives = Solitaire.TextToFives(outputString)
        outf.write(outputFives+"\n")
    else:
        outf.write(outputString+"\n")

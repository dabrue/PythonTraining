#!/bin/env python3
"""
"""
import re

def ProcessTable(textable):
    """
        This function processes a string of text containing the entirety of a
        latex table. It returns a string of text that reformats the table
        as an html table.
    """
    pass

def ProcessMath(texmath):
    pass

def ProcessBlockQuote(texquote):
    pass

def ProcessList(texquote):
    pass

def ProcessItalic(texquote):
    pass

def ProcessItemize(texquote):
    pass

def ProcessEnumerate(texquote):
    pass

def ProcessSection(texquote):
    pass

def ProcessSubsection(texquote):
    pass

def ProcessSubsubsection(texquote):
    pass

def ProcessChapter(texquote):
    pass

def ProcessCode(texquote):
    pass

def ProcessFont(texquote,mod):
    pass



if (__name__ == "__main__"):

    import sys
    import os
    import re
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Convert LaTeX to HTML")
    parser.add_argument("-o","--output",nargs=2,
        help="output file (optional, if not renaming .tex to .html")
    parser.add_argument("InputFile",action=store,
        help="The input .tex file for conversion")

    # Next parse the arguments. The parse_args method does not accept the 
    # calling routine as an argument, but sys.argv will include it as element 0. 
    # Therefore, drop this before sending the other arguments to parse_args
    arguments=sys.argv[1:]
    parser.parse_args(arguments)


    # Assuming that the input file is provided on the command line
    if (len(sys.argv) != 2):
        print("synopsis: ./texhtml.py <texfile>")
        exit(1)
    else:
        inputFileName = sys.argv[1]
        try:
            texf=open(inputFileName,"r")
        except IOError:
            print("File "+inputFileName+" not found.")
            exit(2)

    outfilename = re.sub("\.tex$","\.html",inputfilename)

    texinput = texf.readlines()

    States=["text",
            "italic",
            "bold",
            "math",
            "code",
            "blockquote",
            "image",
            "table",
            "link",
            "chapter",
            "section",
            "subsection",
            "subsubsection",
            "footnote",
            "small",
            "tiny",
            "large",
            "Large",
            "Huge",
            "itemize",
            "enumerate"]

#!/bin/env python3
"""
    Implementation of Solitaire Algorithm and Variants

    In all of the documentation, consider that the Solitaire algorithm
    operates on a deck of cards that are face up. 
"""

__author__   = "Daniel Alan Brue"
__email__    = "danielbrue@gmail.com"
__PGPKeyID__ = "2DFDF230"
__status__   = "Development"
__copyright__= "None"
__version__  = "0.5"

##########################################################################################

# Constant lists for converting the streams of characters to numbers and back. 

N2A= {0:"a", 1:"b", 2:"c", 3:"d", 
      4:"e", 5:"f", 6:"g", 7:"h", 
      8:"i", 9:"j",10:"k",11:"l",
     12:"m",13:"n",14:"o",15:"p",
     16:"q",17:"r",18:"s",19:"t",
     20:"u",21:"v",22:"w",23:"x",
     24:"y",25:"z",26:"A",27:"B", 
     28:"C",29:"D",30:"E",31:"F", 
     32:"G",33:"H",34:"I",35:"J",
     36:"K",37:"L",38:"M",39:"N",
     40:"O",41:"P",42:"Q",43:"R", 
     44:"S",45:"T",46:"U",47:"V",
     48:"W",49:"X",50:"Y",51:"Z", 
     52:"$",53:'%'} # Last two are for jokers A, B

A2N= {"a": 0,"b": 1,"c": 2,"d": 3,
      "e": 4,"f": 5,"g": 6,"h": 7,
      "i": 8,"j": 9,"k":10,"l":11,
      "m":12,"n":13,"o":14,"p":15,
      "q":16,"r":17,"s":18,"t":19,
      "u":20,"v":21,"w":22,"x":23,
      "y":24,"z":25,"A":26,"B":27,
      "C":28,"D":29,"E":30,"F":31,
      "G":32,"H":33,"I":34,"J":35,
      "K":36,"L":37,"M":38,"N":39,
      "O":40,"P":41,"Q":42,"R":43,
      "S":44,"T":45,"U":46,"V":47,
      "W":48,"X":49,"Y":50,"Z":51,
      "$":52,"%":53} # Last two are for jokers A, B

Num2Out = \
    { 0:"A", 1:"B", 2:"C", 3:"D", 
      4:"E", 5:"F", 6:"G", 7:"H", 
      8:"I", 9:"J",10:"K",11:"L", 
     12:"M",13:"N",14:"O",15:"P",
     16:"Q",17:"R",18:"S",19:"T",
     20:"U",21:"V",22:"W",23:"X",
     24:"Y",25:"Z",26:"A",27:"B",
     28:"C",29:"D",30:"E",31:"F", 
     32:"G",33:"H",34:"I",35:"J",
     36:"K",37:"L",38:"M",39:"N",
     40:"O",41:"P",42:"Q",43:"R",
     44:"S",45:"T",46:"U",47:"V",
     48:"W",49:"X",50:"Y",51:"Z",
     52:"",53:""}  # jokers do not output

AZ2N = \
    {"A": 1,"B": 2,"C": 3,"D": 4,
     "E": 5,"F": 6,"G": 7,"H": 8,
     "I": 9,"J":10,"K":11,"L":12,
     "M":13,"N":14,"O":15,"P":16,
     "Q":17,"R":18,"S":19,"T":20,
     "U":21,"V":22,"W":23,"X":24,
     "Y":25,"Z":26}


##########################################################################################

def TripleCut(Deck,JokerA,JokerB,direction="forward"):
    """
        Perform the triple cut on the deck.

        This operation is self-reversing. Take all cards
        above the 'top' joker and swap them with all the cards
        below the 'bottom' joker. 
    """
    ja_indx = Deck.index(JokerA)
    jb_indx = Deck.index(JokerB)
    jmin = min([ja_indx,jb_indx])
    jmax = max([ja_indx,jb_indx])+1
    Deck=Deck[jmax:]+Deck[jmin:jmax]+Deck[:jmin]
    return Deck

##########################################################################################

def CountCut(Deck,direction="forward"):
    """
        Perform the Count Cut on the Deck

        Where the index is the position of the first card on the 
        "bottom" of the cut, and becomes the new top card. 

        That is, "index" represents how many cards to count
        down from the top of the deck. 
    """
    endex=len(Deck)-1
    index=Deck[endex]
    if (direction == "forward"):
        Deck = Deck[index:endex] + Deck[:index] + [Deck[endex]]
    elif (direction == "reverse"):
        midex = endex-index
        Deck = Deck[midex:endex] + Deck[:midex] + [Deck[endex]]
    
    return Deck

##########################################################################################

def ShiftCard(Deck,N,nshift,direction="forward",ident="index",GhostCard=False):
    """
        Shift the card at 'N' by 'nshift' places
        
        Consider the deck of cards to be a ring; if the card is on 
        the bottom of the deck, the next spot is below the top 
        card. 
    
        If nshift is positive, the card is moved "down" toward the 
        bottom of the deck. This is normal mode of operation. 
        If nshift is negative, the card is moved "up" toward the top of
        the deck. This is useful for running the traditional Solitaire
        algorithm in reverse. 

        There is an oddity in the definition of the cipher. A card cannot
        ever land on index 0 (top of the stack). If a card is at the bottom
        of the deck and is shifted one place, it gets placed at index 1, 
        and becomes the card under the top card. 
        
        If optional argument "GhostCard" is set to True, then when shifting
        there is an imaginary extra card between the top and bottom of the
        deck, allowing the shifted card to land on index 0. This means that
        moving the card from the bottom of the deck to the top counts
        as a shift. 
    """
    endex = len(Deck) - 1

    if (ident == "index"):
        index = N
    elif (ident == "value"):
        index = Deck.index(N)
    else:
        print("ERROR: ShiftCard argument, ident=<index|value>")
        exit()

    # Determine new index position
    if (direction == "forward"):
        if (GhostCard):
            M = index + nshift
            l = len(Deck)
            newdex = M % l
        else:
            # This is the original algorithm. 
            M = index + nshift
            print("M",M,N)
            lm1 = len(Deck)-1
            newdex = M % lm1

    elif (direction == "reverse"):
        if (GhostCard):
            M = index - nshift
            l = len(Deck)
            newdex = M % l
        else:
            # This is the original algorithm. 
            M = index - nshift
            lm1 = len(Deck)-1
            newdex = M % lm1

    else:
        print("ERROR: ShiftCard argument, direction=<forward|reverse>")

    Card = Deck[index]

    if (index < newdex):
        Deck.pop(index)
        Deck.insert(newdex,Card)
    elif(index > newdex):
        Deck.pop(index)
        Deck.insert(newdex,Card)
    else:
        pass

    return Deck

##########################################################################################
def Sanitize_String(text):
    import re
    text=text.upper()
    text=re.sub('1', 'ONE ' , text)
    text=re.sub('2', 'TWO '  , text)
    text=re.sub('3', 'THREE ', text)
    text=re.sub('4', 'FOUR ', text)
    text=re.sub('5', 'FIVE ', text)
    text=re.sub('6', 'SIX ',  text)
    text=re.sub('7', 'SEVEN ', text)
    text=re.sub('8', 'EIGHT ', text)
    text=re.sub('9', 'NINE ', text)
    text=re.sub('[^A-Z]','', text)
    return text

##########################################################################################

def TelegraphStyle(text):
    """
        Convert text to telegraph style by writing out punctuation
    """
    import re

    text=text.upper()
    Conversions={
    "0":"ZERO", "1":"ONE", "2":"TWO", "3":"THREE", "4":"FOUR",
    "5":"FIVE", "6":"SIX", "7":"SEVEN", "8":"EIGHT", "9":"NINE",
    "\.":"STOP", ",":"COMMA", ":":"COLON",";":"SEMICOLON",
    "\?":"QUERY","!":"EXCLAMATION","%":"PERCENT","&":"AND",
    "@":"AT"}

    for i in Conversions.keys():
        text=re.sub(i,Conversions[i],text)

    text=re.sub("[^A-Z]","",text)

    return text

##########################################################################################
def TextToFives(text):
    """ 
        Convert uninterrupted string of text into blocks of 5 letters
        and 12 groups per line
    """
    
    new=text[0]
    for i in range(1,len(text)):
        if (i%50 == 0):
            new = new + "\n"
        elif (i%5 == 0):
            new = new + " "
            
        new = new + text[i]

    return new

##########################################################################################
def StringToList(string):
    """
        As the name implies, this converts a string to a list of numbers. For clarity
        reasons, this routine is expecting the string to only contain A-Z characters. 
        Any debugging of the string must happen in the calling routine. 
    """
    import re
    if (re.match("[^A-Z]",string)):
        return 2
    

##########################################################################################
def CombineStreams(mode, stream1, stream2, modulus):
    """ 
        Perform addition or subtraction on two streams with given modulus. 
        This routine will accept strings or lists
        
        arguments are (mode, stream1, stream2, modulus)

        mode must be "add","subtract",or "multiply"

        The streams can be strings of letters, uppercase only, or a list of 
        numbers. 

        modulus - integer for addition, subtraction, and multiplication for modular
            arithmetic
    """
    if (type(stream1) == type("string")):



    

##########################################################################################
# Define the classic Solitaire cipher class
class Cipher:
    """
        This is the classic Solitaire algorithm developed by Bruce Schneier
    """

    import re

    def __init__(self,Key,DeckSize=54,GhostCard=False,
                shiftA=1,shiftB=2,KeyCaseSensitive=False):
        self.Deck = list(range(DeckSize))

        # Now key the deck 
        if (type(Key) == str):
            # strip anything that isn't a letter from the key
            CleanKey = re.sub("[^a-zA-Z]","",Key)
            if (KeyCaseSensitive):
                pass
            else:
                CleanKey = CleanKey.lower()
            for i in range(len(str)):
                #FIXME
                pass
        elif (type(Key) == list):
            #FIXME
            pass
            

        
    def AddKey(self,key):
        pass



if (__name__ == "__main__"):

    import sys
    import unittest

    choice = "init"
    while (choice != "quit"):
    choice = raw_input("Selection: ")

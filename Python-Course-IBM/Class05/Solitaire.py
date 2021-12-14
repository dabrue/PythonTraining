"""
    This module contains a class for the Solitaire Cipher algorithm as well
    as the functions that perform the algorithm steps. 

"""

__author__      = "Daniel A. Brue"
__email__       = "dabrue@us.ibm.com"
__status__      = "Production"

##########################################################################################
def shiftJokerA(deck,debug=False):
    """
        shift joker A down one card. If it is the last card, then it moves to be 
        the second card in the deck (under the top card)
    
        joker A is value 52
    """
    if (deck[53] == 52):  # joker A is the last card
        deck.pop(53)       # remove value at position 53
        deck.insert(1,52)  # insert the value 52 into position 1
    else:  # joker A is not the last card
        jAindex = deck.index(52)  # get index of joker A
        deck.pop(jAindex)
        deck.insert(jAindex+1,52)  # reinsert joker A one position 'down'

    return deck

##########################################################################################
def shiftJokerB(deck,debug=False):
    """ 
        shift joker B down two cards. If it is the last card or second do last, then
        it wraps around the deck. If it is the last card, it moves to be the third
        in the deck (position index 2). If it is the second to last card, it moves to be 
        second in the deck (position index 1).

        joker B is value 53
    """
    if (deck[53] == 53):  # joker B is the last card
        deck.pop(53)
        deck.insert(2,53)
    elif (deck[52] == 53):  # joker B is second to last card
        deck.pop(52)
        deck.insert(1,53)
    else:  # joker B is not the last or penultimate card
        jBindex = deck.index(53)
        deck.pop(jBindex) 
        deck.insert(jBindex+2,53)

    return deck


##########################################################################################
def tripleCut(deck,debug=False):
    """ 
        Find both jokers. Take all cards above the top joker and swap them with all
        cards beneith the bottom joker. 
    """
    jA = 52
    jB = 53

    jAindex = deck.index(jA)
    jBindex = deck.index(jB)

    jmin = min(jAindex,jBindex)   # find the "first" joker
    jmax = max(jAindex,jBindex)   # find the "second" joker

    top = deck[:jmin]  # create a new list of all cards up to the first joker
    middle = deck[jmin:jmax+1] # jmax + 1 because the notation does not include the last 
    bottom = deck[jmax+1:] 

    # generate a new deck. "+" concatenates lists
    deck = bottom + middle + top
    return deck


##########################################################################################
def countCut(deck,debug=False):
    """
        Perform the count cut operation. Look at the bottom card and convert it to 
        a value N. Set the card aside. Count N cards down from the top and swap them
        with the cards on the bottom. Return the card set aside to the bottom of the deck
    """
    N = deck.pop(53)

    # If we found joker B, use the value 52 instead of 53. 
    if (N == 53):
        Cutpoint = 52
    else:
        Cutpoint = N
    
    # now reassemble the deck, swapping bottom and top card stacks
    # remember indexing needs N to be incremented by 1 so that the Nth card
    # is in the top half of the deck. 
    deck = deck[Cutpoint+1:] + deck[:Cutpoint+1]

    # reinsert the bottom card
    deck.insert(53,N)

    return deck


##########################################################################################
def getOutput(deck,debug=False):
    """
        Find the output value. Turn the top card into a numeric value, and count that many
        cards down in the deck. The next card is the output card. 
    """
    index = deck[0]
    if (index == 53): # if the top card is joker B, give it a value of joker A
        index = 52
    value = deck[index+1]
    return value

##########################################################################################
def keyDeck(deck,key,debug=False):

    if (type(key) == type("a")):
        cleanKey = sanitizeText(key)
        key = textToNumbers(cleankey)
    elif (type(key) == type([])):
        # all OK, this is expected. 
        pass
    else:
        print("Unrecognized key type")
        exit(1)

    for i in range(len(key)):
        keycut = key+1  # to account for 0-25 range of key when countin 1-26 cards

        if (keycut < 1 or keycut > 26):
            print("Key Error: out of range")
            print("key card is value ",keycut)
            exit(1)

        deck = shiftJokerA(deck,debug)
        deck = shiftJokerB(deck,debug)
        deck = tripleCut(deck,debug)
        deck = countCut(deck,debug)

        # Now perform a key-cut. This is similar to the countCut, but instead of using the
        # bottom card's value as the cut point, use the key stream value. 
        # Like the count cut, keep the bottom card aside. 

        upper = deck[:keycut]
        lower = deck[keycut:-1] # range from keycut to second to last card
        deck = lower+upper+[deck[-1]]

    # the deck has now been keyed according to the key string. 
    return deck

    
##########################################################################################
def sanitizeText(text,debug=False):
    """
        strip a text string of everything but letters
    """
    import re
    if (type(text) != type("a")):
        print("text not string")
        print(text)
        exit(1)
    
    text=text.upper()  # all text to upper case
    
    # remove everything that is not A-Z
    text = re.sub("[^A-Z]","",text)

    return text
    
##########################################################################################
def textToNumbers(text,debug=False):
    """
        Convert text string to a numeric list
    """
    text2 = sanitizeText(text,debug)
    numbers = []
    # map letters to numbers from 0 to 25
    for i in range(len(text2)):
        numbers.append(ord(text2[i])-65)

    return numbers


##########################################################################################
def numbersToText(numbers,debug=False):
    """
        Convert numbers to letters. If 'numbers' is a single integer, the string
        returned is a single character. If 'numbers' is a list, the string returned
        is a string of each corresponding letter.
    """
    if (type(numbers) == int):
        # convert single number to character. 
        string = chr(numbers+65)  # convert by ascii mapping

    elif (type(numbers) == list):
        string = ""
        for i in numbers:
            #print(i)
            string=string+chr(i+65)

    return string


##########################################################################################

def TextToFives(text):
    """ 
        Convert uninterrupted string of text into blocks of 5 letters
        and 10 groups per line
    """

    new=text[0]
    for i in range(1,len(text)):
        if (i%50 == 0):
            new = new + "\n"
        elif (i%5 == 0):
            new = new + " "

        new = new + text[i]

    new=new+"\n"

    return new



##########################################################################################
class SolitaireCipher:

    #-------------------------------------------------------------------------------------
    def __init__(self):
        self.deck=list(range(54))

    
    #-------------------------------------------------------------------------------------
    def reset(self):
        self.deck=list(range(54))

    #-------------------------------------------------------------------------------------
    def keyDeck(self,keystring):

        keyClean = sanitizeText(keystring)
        keyNumbers = textToNumbers(keyClean)

        for i in range(len(keyNumbers)):
            self.deck=shiftJokerA(self.deck)
            self.deck=shiftJokerB(self.deck)
            self.deck=tripleCut(self.deck)
            self.deck=countCut(self.deck)
        
            # now perform the key cut. Like count cut, but cut on the key value
            # instead of the bottom card value. Still keep the bottom card unmoved.
            BottomCard = self.deck.pop(53)

            cut = keyNumbers[i]+1
            self.deck=self.deck[cut:] + self.deck[:cut] 
            self.deck.insert(53,BottomCard)


    #-------------------------------------------------------------------------------------
    def encrypt(self,plaintext):
        """
            Perform the encryption operation. Return ciphertext
        """

        
        plaintextClean = sanitizeText(plaintext)

        Nout = len(plaintextClean)

        keyStream = self.outputOnly(Nout, skipJokers=True, AZRange=1)
        plainStream = textToNumbers(plaintextClean)


        cipherStream= []
        for i in range(len(keyStream)):

            # Add the letters (A=1, B=2, ...)
            C = (plainStream[i]+keyStream[i] +2)  # plus 2 so A-Z is 1-26

            # Ensure range 1-26
            while (C > 26):
                C -= 26
            
            C -= 1 # put on range 0-25
            cipherStream.append(C)

        ciphertext = numbersToText(cipherStream)
        

        return ciphertext

    #-------------------------------------------------------------------------------------
    def decrypt(self,ciphertext):
        """
            Perform the decryption operation. Return the plaintext. 
        """
        ciphertextClean = sanitizeText(ciphertext)
        Nout = len(ciphertextClean)
        keyStream = self.outputOnly(Nout,skipJokers=True, AZRange=1)
        cipherStream = textToNumbers(ciphertextClean)

        plainStream=[]
        print("lenkeystream",len(keyStream))
        for i in range(len(keyStream)):
        
            # if this subtraction produces 0, the letter should be Z
            P = (cipherStream[i] - keyStream[i]) 
            while (P <= 0):
                P += 26     # put on range 1-26
            P -= 1          # put on range 0-25
            plainStream.append(P)

        plaintext = numbersToText(plainStream)

            
        return plaintext

    #-------------------------------------------------------------------------------------
    def outputOnly(self,N,skipJokers=False,AZRange = 2):
        """
            Return a list of N numbers from the output of the algorithm. 
            
            Optional argument 'skipJokers' is default False, so jokers will
            be included in the returned list. If this is set to True, then
            this method will only return cards that are valid characters. 
    
            Optional argument 'AZRange' is default 2, which means the output
            list will be span A-Z twice, on the range 0-53. If set to 1, then
            the output will be on the range 0-25
        """

        outputList = []

        if (skipJokers):
            count=0
            while (count < N):
                self.deck=shiftJokerA(self.deck)
                self.deck=shiftJokerB(self.deck)
                self.deck=tripleCut(self.deck)
                self.deck=countCut(self.deck)
                output=getOutput(self.deck)
                if (output >= 52):
                    continue
                else:
                    count += 1
                    outputList.append(output)
        else:
            for i in range(N):
                self.deck=shiftJokerA(self.deck)
                self.deck=shiftJokerB(self.deck)
                self.deck=tripleCut(self.deck)
                self.deck=countCut(self.deck)
                output=getOutput(self.deck)
                outputList.append(output)

        if (AZRange == 1):
            for i in range(len(outputList)):
                if (outputList[i] > 25):
                    outputList[i] -= 26

        return outputList

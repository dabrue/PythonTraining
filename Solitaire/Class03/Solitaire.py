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
        N = 52
    
    # now reassemble the deck, swapping bottom and top card stacks
    # remember indexing needs N to be incremented by 1 so that the Nth card
    # is in the top half of the deck. 
    deck = deck[N+1:] + deck[:N+1]

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
    key = []
    # map letters to numbers from 0 to 25
    for i in range(len(text2)):
        key.append(ord(text2[i])-65)

    return key


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

        ciphertext = ""
        outputCount = 0
        while (outputCount < len(plaintextClean)):

            # get next plaintext character
            plainChr=textToNumber(plaintextClean[outputCount])

            # Operate on the deck
            self.deck=shiftJokerA(self.deck)
            self.deck=shiftJokerB(self.deck)
            self.deck=tripleCut(self.deck)
            self.deck=countCut(self.deck)
            output=getOutput(self.deck)


            # if we get a joker on output, skip it and reiterate the algorithm. 
            # Otherwise, increment the counter. 
            if (output >= 52):
                continue 
            else:
                outputCount += 1

            # make sure the output is in the range 0 to 25, since the deck doubles
            # the number of letters in the alphabet. A = 0 = 26
            if (output > 25):
                output -= 26
            
            # Add the cards, e.g., A + B = C
            # since python indexes from 0, and A=0 in the deck, we add one to make
            # sure that the modular arithmetic works correctly. We need Z to be the
            # identity element in modular addition. 
            # Since A = 0, B=1, C=2, to perform this correctly we need to add one to 
            # each card, perform the modular addition, then subtract one. 
            C = ((plainChr+1) + (output+1)) % 26 - 1
            cipherChr = numberToText(C)
            ciphertext = ciphertext + cipherChr
        
        return ciphertext

    #-------------------------------------------------------------------------------------
    def decrypt(self,ciphertext):
        """
            Perform the decryption operation. Return the plaintext. 
        """
        ciphertextClean = sanitizeText(ciphertext)

        plaintext = ""
        outputCount = 0
        while (outputCount < len(ciphertextClean)):

            # get next plaintext character
            cipherChar=textToNumber(ciphertextClean[outputCount])

            # Operate on the deck
            self.deck=shiftJokerA(self.deck)
            self.deck=shiftJokerB(self.deck)
            self.deck=tripleCut(self.deck)
            self.deck=countCut(self.deck)
            output=getOutput(self.deck)


            # if we get a joker on output, skip it and reiterate the algorithm. 
            # Otherwise, increment the counter. 
            if (output >= 52):
                continue 
            else:
                outputCount += 1

            # make sure the output is in the range 0 to 25, since the deck doubles
            # the number of letters in the alphabet. A = 0 = 26
            if (output > 25):
                output -= 26
            
            # Add the cards, e.g., A + B = C
            # since python indexes from 0, and A=0 in the deck, we add one to make
            # sure that the modular arithmetic works correctly. We need Z to be the
            # identity element in modular addition. 
            # Since A = 0, B=1, C=2, to perform this correctly we need to add one to 
            # each card, perform the modular addition, then subtract one. 
            P = ((cipherChar+1) - (output+1)) % 26 - 1
            plainChr = numberToText(P)
            plaintext = plaintext + plainChar
        
        return plaintext

    #-------------------------------------------------------------------------------------
    def outputOnly(self,N,skipJokers=False):
        """
            Return a list of N numbers from the output of the algorithm. 
            
            Optional argument 'skipJokers' is default False, so jokers will
            be included in the returned list. If this is set to True, then
            this method will only return cards that are valid characters. 
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

        return outputList

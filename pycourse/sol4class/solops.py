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
    jmax = min(jAindex,jBindex)   # find the "second" joker

    top = deck[:jmin]  # create a new list of all cards up to the first joker
    middle = deck[jmin:jmax+1] # jmax + 1 because the notation does not include the last 
    bottom = deck[jmax+1:] 

    # generate a new deck. "+" concatenates lists
    deck = bottom + middle + top
    return deck


##########################################################################################
def countCut(deck,debug=False):


##########################################################################################
def getOutput(deck,debug=False):
    """
        Find the output value. Turn the top card into a numeric value, and count that many
        cards down in the deck. The next card is the output card. 
    """
    index = deck[0]
    if (index = 53): # if the top card is joker B, give it a value of joker A
        index = 52
    value = deck[index+1]
    return value

##########################################################################################
def keyDeck(deck,key,debug=False):

    if (type(key) == type("a")):
        cleanKey = sanitizeText(key)
        key = textToNumbers(cleankey)
    elif (type(key) == type([]):
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
    if (type(text) != type("a"):
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

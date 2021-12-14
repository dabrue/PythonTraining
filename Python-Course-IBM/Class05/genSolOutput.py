#!/bin/env python3
import Solitaire

if (__name__ == "__main__"):

    NOutput = 1000000000

    Cipher = Solitaire.SolitaireCipher()

    # get the key file
    with open("MajorGeneral","r") as f:
        filekey=f.read()
    key = Solitaire.sanitizeText(filekey)
    Cipher.keyDeck(key)

    NumericOutput = Cipher.outputOnly(NOutput,skipJokers=True,AZRange=2)
    
    outf=open("NumericOutput01B52","w")
    for i in range(len(NumericOutput)):
        outf.write(str(NumericOutput[i])+"\n")
    outf.close()
        

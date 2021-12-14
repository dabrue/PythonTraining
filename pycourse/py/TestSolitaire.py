#!/bin/env python3
import math

import Solitaire
import unittest

print(math.log(math.factorial(54),2))

Deck = list(range(10)) + [4]
print(type(Deck))

NewDeck = Solitaire.CountCut(Deck)

print(NewDeck)

ThreeDeck = Solitaire.CountCut(NewDeck,direction="reverse")

print(ThreeDeck)

fourDeck = Solitaire.ShiftCard(Deck,5,-2)
print(fourDeck)


# Just testing the text cleaning routines

text="THis & is Some test text. Email@organization.org? * 9()"

newtext = Solitaire.TelegraphStyle(text)
print(text)
print(newtext)
fivetext = Solitaire.TextToFives(newtext)
print(fivetext)

#!/bin/env python3
"""
    2013-11-04
    Class 07: Unit testing with unittest

    For today's class, we will look at Python's unittest module and how to 
    use it to create a series of tests for our Solitaire implmentation. 

    We have not yet used any modules or libraries that behave quite like unittest. The
    unittest module provides a framework for testing other routines, but it recognizes
    tests based on the class type and method name. See comments in this code for
    further explanations. 

"""

__author__      = "Daniel A. Brue"
__email__       = "dabrue@us.ibm.com"

"""
    Assertion Methods:

        assertEqual(a, b)           a == b   
        assertNotEqual(a, b)        a != b   
        assertTrue(x)               bool(x) is True      
        assertFalse(x)              bool(x) is False     
        assertIs(a, b)              a is b
        assertIsNot(a, b)           a is not b
        assertIsNone(x)             x is None
        assertIsNotNone(x)          x is not None
        assertIn(a, b)              a in b
        assertNotIn(a, b)           a not in b
        assertIsInstance(a, b)      isinstance(a, b)
        assertNotIsInstance(a, b)   not isinstance(a, b)
"""

import Solitaire
import unittest
import random

class deckIntegrity(unittest.TestCase):
    import random
    """
        This series of tests ensures that after every operation on our
        deck of cards, we maintain that all the cards are accounted for. 
        This ensures that we haven't mistakenly lost or added any cards or
        changed their values. 
    """

    # "setUp" is a specially named function, like __init__ for standard classes. 
    # It will be run by unittest to set up local variables and definitions prior
    # to running any of the test routines. 
    def setUp(self):
        """
            set up constants to test the deck against
        """
        self.decklist=list(range(54))
        random.seed()
    
    
    # the test functions that are automatically run must begin with "test"
    def test_shiftJokerA(self):
        # create a sample deck
        deck = list(range(54))
        # shift joker A
        newdeck = Solitaire.shiftJokerA(deck)
        # now test that we haven't lost or gained any cards
        for card in newdeck:
            self.assertIn(card,self.decklist)
        # Test again with a randomly shuffled deck

    def test_shiftJokerB(self):
        # create a sample deck
        deck = list(range(54))
        # shift joker B
        newdeck = Solitaire.shiftJokerB(deck)
        # now test that we haven't lost or gained any cards
        for i in newdeck:
            self.assertIn(i,self.decklist)

    def test_tripleCut(self):
        # generate a new ordered deck
        deck = list(range(54))
        # shuffle the deck in place
        random.shuffle(deck)
        newdeck = Solitaire.tripleCut(deck)
        for i in newdeck:
            self.assertIn(i,self.decklist)

    def test_countCut(self):
        # generate a new ordered deck
        deck = list(range(54))
        # shuffle the deck in place
        random.shuffle(deck)
        newdeck = Solitaire.tripleCut(deck)
        for i in newdeck:
            self.assertIn(i,self.decklist)
        #self.assertIn(60,self.decklist)
        for i in self.decklist:
            self.assertIn(i,newdeck)
        self.assertNotEqual(newdeck,self.decklist)
        newdeck.sort()
        self.assertEqual(newdeck,self.decklist)

    def tearDown(self):
        # If the cipher had closing methods, it would go here. 
        pass


class outputTesting(unittest.TestCase):

    def setUp(self):
        self.cipher=Solitaire.SolitaireCipher()
        random.shuffle(self.cipher.deck)
        self.decklist=list(range(54))

    # Example of using a function "decorator" to skip a test
    @unittest.skip("Redundant Test")
    def test_outputRangeCheck(self):
        pass 

    @unittest.expectedFailure
    def test_wrongValue(self):
        unittest.assertEqual(self.cipher.deck[0] == -1)



if (__name__ == "__main__"):
    unittest.main(verbosity=2)

#!/bin/env python
import pickle


class whatever:
    def __init__(self):
        self.a=1
        self.b=2


A=[]
for i in range(11):
    A.append(whatever()) 


filename="test.pickle"

pickle.dump(A,open(filename,"w"))



#!/bin/env python3
'''
    Test script for generators
'''

__author__ = 'Daniel Brue'

def gen1(N):

    while (True):
        yield 1


if (__name__ == '__main__'):
    for i in gen1(1):
        print(i)

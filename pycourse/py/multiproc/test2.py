#!/bin/env python3
import multiprocessing as mp
import os

def getnums(N):
    import random
    import time
    nums=[]
    t=random.randint(1,3)
    time.sleep(t)
    for i in range(N):
        a=random.randint(0,5)
        nums.append(a)
    return nums


if (__name__ == "__main__"):
    
    pool=mp.Pool(processes=None)  # will use number of cpus by default
    NumArgs=list(range(1,10))
    result=pool.map(getnums,NumArgs)
    pool.close()
    for i in result:
        print(i)

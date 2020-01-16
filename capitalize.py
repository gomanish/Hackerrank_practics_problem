#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    go=True
    word=[]
    for w in s.split():
        word.append(w.capitalize())
    temp=''
    i=0
    for w1 in s:
        if w1 == ' ':
            temp=temp+w1
            go=True
        else:
            if go:
                temp=temp+word[i]
                i+=1
                go=False
    return temp

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

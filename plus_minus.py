#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(n,arr):
    # Write your code here
    posi=0
    neg=0
    zero=0
    
    for i in arr:
        if i>0:
            posi+=1
        if i<0:neg+=1
        if i==0:zero+=1
    print(posi/n)
    print(neg/n)
    print(zero/n)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n,arr)

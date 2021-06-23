#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if "PM" in s:
        if "12"!=s[:2]:
            updated=str(int(s[:2])+12)
            s=updated+s[2:]
    elif "AM" in s:
        if "12"==s[:2]:
            updated="00"
            s=updated+s[2:]
    return s[:8]

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

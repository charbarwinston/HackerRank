#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    pos, valleys = 0, 0
    inValley = False
    for c in s:
        if c == 'U':
            pos += 1
            if pos == 0:
                valleys += 1
        else:
            pos -= 1
    return valleys 
if __name__ == '__main__':
    print(countingValleys(8, "DUDU"))

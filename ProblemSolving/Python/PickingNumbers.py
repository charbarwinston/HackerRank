#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(a):
    counts = dict()
    for num in a:
        counts[num] = counts.get(num, 0) + 1
    print(counts)
    sortedKeys = sorted(counts.keys())
    globalMax = -1
    for i in range(0, len(sortedKeys)-1):
        if abs(sortedKeys[i] - sortedKeys[i-1]) <= 1:
            localMax = counts[sortedKeys[i]] + counts[sortedKeys[i-1]]
            if localMax > globalMax:
                globalMax = localMax
    if globalMax != -1 and globalMax > max(counts.values()):
        return("globalMax")
    else:
        return(max(counts.values()))

if __name__ == '__main__':
    a = [4,6,5,3,3,1]
    print(pickingNumbers(a))
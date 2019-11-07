#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(ar):
    count = 0
    combos = itertools.combinations(ar, 2)
    for value in combos:
        if sum(value)%5 == 0:
            count = count + 1
        print(value)
    return 0

if __name__ == '__main__':
    divisibleSumPairs([1, 2, 3, 4, 5])

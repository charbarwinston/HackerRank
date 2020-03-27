#!/bin/python3

import math
import os
import random
import re
import sys

ms1 = [[8,1,6],[3,5,7],[4,9,2]]
ms2 = [[8,3,4],[1,5,9],[6,7,2]]
ms3 = [[4,3,8],[9,5,1],[2,7,6]]
ms4 = [[4,9,2],[3,5,7],[8,1,6]]
ms5 = [[2,9,4],[7,5,3],[6,1,8]]
ms6 = [[2,7,6],[9,5,1],[4,3,8]]
ms7 = [[6,7,2],[1,5,9],[8,3,4]]
ms8 = [[6,1,8],[7,5,3],[2,9,4]]
knownSquares = [ms1,ms2,ms3,ms4,ms5,ms6,ms7,ms8]

# Lol bruteforce
def formingMagicSquare(s):
    lowest = sys.maxsize
    for ms in knownSquares:
        cost = calulateDistance(s, ms)
        if cost < lowest:
            lowest = cost
    return lowest 

def calulateDistance(s, ms):
    sum = 0
    for rowNumber,row in enumerate(s):
        for index, number in enumerate(row):
            if number != ms[rowNumber][index]:
                sum += abs(number - ms[rowNumber][index])
    return sum

if __name__ == '__main__':

    s = [[5,3,4],[1,5,8],[6,4,2]]
    print(calulateDistance(s, ms2))



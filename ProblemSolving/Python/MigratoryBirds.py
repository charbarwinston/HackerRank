#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    types = {}
    for bird in arr:
        if (bird in types):
            types[bird] = types[bird] + 1
        else:
            types[bird] = 1;
    maxValue = 0
    maxKey = 0
    for key in sorted(types.keys()):
        if types[key] > maxValue:
            print("For key: ", key, " ",types[key], " is greater than ", maxValue)
            maxKey = key
            maxValue = types[key]
    return maxKey


if __name__ == '__main__':
    pass

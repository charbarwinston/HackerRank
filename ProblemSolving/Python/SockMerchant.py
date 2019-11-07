#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = {}
    pairs = 0
    for sock in ar:
        if sock in socks:
            pairs = pairs + 1
            del socks[sock]
        else:
            socks[sock] = 1
    return pairs
if __name__ == '__main__':

    result = sockMerchant(10, [1, 1, 3, 1, 2, 1, 3, 3, 3, 3])

    print(str(result) + '\n')


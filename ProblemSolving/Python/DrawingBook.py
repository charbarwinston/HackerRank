#!/bin/python3

import os
import sys


def pageCount(n, p):
    n = int(n)
    p = int(p)
    print (int(min(p/2, n/2-p/2)))
if __name__ == '__main__':
    print(pageCount(6, 5))

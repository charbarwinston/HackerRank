#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    distanceA = abs(x - z)
    distanceB = abs(y - z)
    closest = min(distanceA,distanceB)
    if (distanceA == closest and distanceB == closest):
        return "Mouse C"
    elif (distanceA == closest):
        return "Cat A"
    elif (distanceB == closest):
        return "Cat B"        

if __name__ == '__main__':

    print(catAndMouse(1, 3, 2))


#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    highest = -1
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                highest = max(highest, keyboard+drive)
            else:
                pass
    return highest

if __name__ == '__main__':
    b = 60

    keyboards = [40, 50, 60]

    drives = [5, 8, 12]

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    print(getMoneySpent(keyboards, drives, b))

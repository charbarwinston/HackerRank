import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    del bill[k]
    total = sum(bill)
    portion = total / 2
    if b == portion:
        return("Bon Appetit")
    else:
        return(abs(portion - b))
        
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)

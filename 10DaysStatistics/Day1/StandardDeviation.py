n = int(input())
X = list(map(int, input().split()))

mean = sum(X)/n

total = 0
for value in X:
    total += ((mean - value)**2)
from math import sqrt
print(round(sqrt((total/n)),1))
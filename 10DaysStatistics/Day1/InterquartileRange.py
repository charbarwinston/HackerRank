n = int(input())
x = list(map(int, input().split()))
f = list(map(int, input().split()))

fullList = []
for element,frequency in zip(x,f):
    for i in range(0, frequency):
        fullList.append(element)
fullList.sort()
from statistics import median
q1 = median(fullList[:len(fullList)//2])
q3 = median(fullList[(len(fullList)+1)//2:])
print (float(q3 - q1))
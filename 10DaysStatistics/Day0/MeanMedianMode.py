# Enter your code here. Read input from STDIN. Print output to STDOUT
X = input();
N = input();

X = int(X)

N = N.split()
N = [int(i) for i in N]
N.sort()

Mean = sum(N,0)/X

MiddleIndex = int(X / 2) - 1

Median = (N[MiddleIndex + 1] + N[(MiddleIndex)]) / 2

uniqueValues = {}
for i in N:
    if i in uniqueValues:
        uniqueValues[i] = uniqueValues[i] + 1
    else:
        uniqueValues[i] = 1

maxValue = 0
maxKey = 0
for key in uniqueValues.keys():
    if uniqueValues[key] > maxValue:
        maxValue = uniqueValues[key]
        maxKey = key

print(Mean)
print(Median)
if maxValue == 1:
    print(N[0])
else:
    print(maxKey)

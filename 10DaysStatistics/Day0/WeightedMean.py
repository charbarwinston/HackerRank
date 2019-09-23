X = input()
N = input()
W = input()

X = int(X)
N = N.split()
W = W.split()

N = [int(i) for i in N]
W = [int(i) for i in W]


weights = sum(W)
total = 0
for i,y in zip(N,W):
    total += i * y

WeightedMean = total / weights
print(round(WeightedMean, 1))    

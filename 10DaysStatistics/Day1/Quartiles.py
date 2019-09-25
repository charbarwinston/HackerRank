import statistics

X = input()
X = int(X)

N = input()
N = N.split()
N = [int(i) for i in N]
N.sort()

Q1, Q2, Q3 = 0, 0, 0

if (X % 2 == 0):
    Q1 = int(statistics.median(N[:int(len(N) / 2) - 1]))
    Q2 = int(statistics.median(N))
    Q3 = int(statistics.median(N[int((len(N) / 2)) - 1:]))
else:
    Q1 = int(statistics.median(N[:int(len(N) / 2)]))
    Q2 = int(statistics.median(N))
    Q3 = int(statistics.median(N[int((len(N) / 2)) + 1:]))
print(Q1)
print(Q2)
print(Q3)
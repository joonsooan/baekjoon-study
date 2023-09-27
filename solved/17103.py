import sys
import math

n = 1000000
a = [True] * (n + 1)
m = int(math.sqrt(n))

for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, n + 1, i):
            a[j] = False

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    result = 0
    for j in range(2, (n // 2) + 1):
        if a[j] and a[n-j]:
            result += 1
    print(result)

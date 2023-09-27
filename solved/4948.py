import sys
import math


n = 123456
a = [True] * (2*n + 1)
m = int(math.sqrt(2*n))

for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, 2*n + 1, i):
            a[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    result = 0
    for i in range(n + 1, 2*n + 1):  # n+1부터 2n까지 소수 개수 구하기
        if a[i] == True:
            result += 1
    print(result)

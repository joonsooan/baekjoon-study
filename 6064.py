import sys

T = int(input())

for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())

i = 1

while True:
    if (i - x) % M == 0 and (i - y) % N == 0:
        print(i)
        break
    else:
        pass

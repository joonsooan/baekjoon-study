import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    res = int((math.sqrt(1 + (8*n)) - 1) // 2)
    print(res)

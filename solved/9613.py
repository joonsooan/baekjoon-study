import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


t = int(sys.stdin.readline())
for i in range(t):
    lst = list(map(int, sys.stdin.readline().split()))
    res = 0
    for j in range(1, len(lst)):
        for k in range(j+1, len(lst)):
            res += gcd(lst[j], lst[k])
    print(res)

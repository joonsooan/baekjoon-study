import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print((a * b // gcd(a, b)))

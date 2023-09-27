import sys
import math


def is_prime_num(n):
    if n == 0 or n == 1:
        return 2
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    while True:
        if is_prime_num(n) == 2:
            print(2)
            break
        elif is_prime_num(n):
            print(n)
            break
        else:
            n += 1

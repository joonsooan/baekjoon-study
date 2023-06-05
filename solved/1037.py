import sys

num_of_divisor  = int(input())
divisors = list(map(int, sys.stdin.readline().split()))
divisors.sort()

# print(num_of_divisor)
# print(divisors)

num = divisors[0] * divisors[len(divisors) - 1]
print(num)
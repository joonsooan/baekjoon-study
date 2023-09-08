import sys
input = sys.stdin.readline

N, K = map(int, input().split())
memoization = [0] * 11


def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif memoization[n] != 0:
        return memoization[n]
    memoization[n] = factorial(n - 1) * n
    return memoization[n]


# 조합 공식 nCk = n!/(n-k)!k!
print(factorial(N) // (factorial(N-K) * factorial(K)))

# n, k = map(int, input().split())
# numerator = 1   # 분자
# denominator = 1  # 분모

# for i in range(1, n + 1):  # 분자의 n!
#     numerator *= i

# for j in range(1, k + 1):  # 분모의 k!
#     denominator *= j

# for k in range(1, n - k + 1):  # 분모의 (n-k)!
#     denominator *= k

# print(int(numerator / denominator))

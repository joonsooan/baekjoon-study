# 단순 중복조합 공식을 이용한 풀이
# n, k = map(int, input().split())
# fac = [1]*(n+k)

# for i in range(1, n+k):
#     fac[i] = fac[i-1] * i

# print((fac[n+k-1] // (fac[k-1] * fac[n])) % 1000000000)

# 규칙을 이용한 풀이
import sys

n, k = map(int, sys.stdin.readline().split())
# dp[n][k]: n, k에 대한 경우의 수
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(k + 1):
    dp[0][i] = 1

for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % (10 ** 9)

print(dp[n][k])

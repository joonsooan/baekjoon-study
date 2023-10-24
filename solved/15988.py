import sys

t = int(sys.stdin.readline())
dp = [0] * (10 ** 6 + 1)
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 10**6 + 1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % (10 ** 9 + 9)

for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])

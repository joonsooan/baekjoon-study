import sys

N = int(input())
table = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
dp = [0] * (N + 1)


# Bottom-Up
for i in range(N):
    for j in range(i + table[i][0], N + 1):
        if dp[j] < dp[i] + table[i][1]:  # dp에 담긴 값보다 계산한 값이 클 때
            dp[j] = dp[i] + table[i][1]  # dp에 더 큰 값을 담아줌

print(dp[-1])


# Top-Down
for i in range(N - 1, -1, -1):
    if i + table[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], table[i][1] + dp[i + table[i][0]])

print(dp[0])

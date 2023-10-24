MOD = 1000000000
n = int(input())
# dp[i][j] -> i자리 계단 수 중 j로 끝나는 것의 개수
dp = [[0 for _ in range(10)] for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:    # ex) 3210 -> 0으로 끝나는 경우는 오직 하나
            dp[i][j] = dp[i-1][1]
        elif j == 9:  # ex) 6789 -> 9로 끝나는 경우는 오직 하나
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % MOD)

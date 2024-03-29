n = int(input())  # 1 <= n <= 1000000
dp = [0] * (n+1)

for i in range(2, n+1):
    # if i % 6 == 0:
    #     dp[i] = min(dp[i-1], dp[i//2], dp[i//3]) + 1
    # elif i % 2 == 0:
    #     dp[i] = min(dp[i-1], dp[i//2]) + 1
    # elif i % 3 == 0:
    #     dp[i] = min(dp[i-1], dp[i//3]) + 1
    # else:
    #     dp[i] = dp[i-1] + 1
    dp[i] = dp[i - 1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[n])

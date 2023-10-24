X = 1000000009
MAX = 100001
t = int(input())
dp = [[0 for _ in range(3)] for _ in range(MAX)]

# [1로 끝나는 경우, 2로 끝나는 경우, 3으로 끝나는 경우]
dp[1] = [1, 0, 0]  # 1
dp[2] = [0, 1, 0]  # 2
dp[3] = [1, 1, 1]  # 2 + 1, 1 + 2, 3

for i in range(4, MAX):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % X  # (2, 3으로 끝나는 숫자) + 1
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % X  # (1, 3으로 끝나는 숫자) + 2
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % X  # (1, 2로 끝나는 숫자) + 3

for i in range(t):
    n = int(input())
    print((dp[n][0] + dp[n][1] + dp[n][2]) % X)

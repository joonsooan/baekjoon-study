n = int(input())
p_lst = list(map(int, input().split()))
p_lst.insert(0, 0)
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = p_lst[i]
    for j in range(1, i):
        dp[i] = min(dp[i], p_lst[j] + dp[i-j])

print(dp[n])

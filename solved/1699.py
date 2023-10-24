n = int(input())
dp = [x for x in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i:
            break
        # (i-j*j) + j*j = i
        # 뒤의 +1은 (i-j*j)에 j*j를 더해줄 때 항이 하나 늘어나는 걸 의미
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1
print(dp[n])

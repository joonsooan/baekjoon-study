n = int(input())
dp = [[0, 0] for _ in range(n+1)]
# dp[i][j] -> i자리 숫자 중 j로 끝나는 수의 개수
dp[1][1] = 1

for i in range(2, n+1):
    # 0은 0, 1 상관없이 붙을 수 있음
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    # i자리 숫자 중 0으로 끝나는 수의 개수 = i-1자리 숫자 중 1로 끝나는 수의 개수
    dp[i][1] = dp[i-1][0]

print(sum(dp[n]))


# 그냥 피보나치 수열과 동일함
n = int(input())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])

n = int(input())
lst = list(map(int, input().split()))
# dp: lst[i]를 마지막 값으로 가지는 가장 긴 증가분수열의 길이
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            # dp[i] = lst[i]가 추가될 수 있는 증가분수열 중 가장 긴 수열의 길이 + 1
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

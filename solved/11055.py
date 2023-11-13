import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = lst[:]  # dp = lst로 할 경우 같은 주소에 할당됨.

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + lst[i])
print(max(dp))

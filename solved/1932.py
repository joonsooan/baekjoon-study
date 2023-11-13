import sys
input = sys.stdin.readline

n = int(input())
lst = [[0]*n for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        lst[i][j] = temp[j]

dp = lst
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] += lst[i-1][j]
        else:
            dp[i][j] += max(lst[i-1][j-1], lst[i-1][j])

print(max(dp[-1]))

import sys
input = sys.stdin.readline

n = int(input())
score_lst = []
dp = [0]
for _ in range(n):
    score_lst.append(int(input()))

dp.append(score_lst[0])  # dp[1]
for i in range(1, n):
    
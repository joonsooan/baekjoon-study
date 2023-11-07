import sys
input = sys.stdin.readline

n, m = map(int, input().split())
time_lst = [int(input()) for _ in range(n)]
start, end = 1, max(time_lst)

# Finding maximum amount of time one person can wait
while start <= end:
    mid = (start + end) // 2

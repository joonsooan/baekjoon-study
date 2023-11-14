import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp1 = lst[:]
min_idx_lst = []
max_lst = []

# 숫자를 제거하지 않는 경우
for i in range(1, n):
    if lst[i] < 0:
        min_idx_lst.append(i)
    dp1[i] = max(dp1[i], dp1[i-1] + dp1[i])
max_lst.append(max(dp1))

# 숫자를 제거하는 경우
for idx in min_idx_lst:
    lst1 = lst[:]
    dp2 = lst1[:]
    lst1 = lst1[:idx] + lst1[idx+1:]
    for i in range(1, n-1):
        dp2[i] = max(lst1[i], dp2[i-1] + lst1[i])
    max_lst.append(max(dp2))

print(max_lst)

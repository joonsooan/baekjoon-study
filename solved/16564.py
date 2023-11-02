import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(int(input()) for _ in range(n))
start, end = min(lst), max(lst) + k

while start <= end:
    mid = (start + end) // 2
    req_lvl = 0
    # Calculating required level for each character
    for lvl in lst:
        if lvl < mid:
            req_lvl += (mid - lvl)
    # Required level is bigger than k -> Goal is too high
    if req_lvl > k:
        end = mid - 1
    else:
        start = mid + 1

print(end)

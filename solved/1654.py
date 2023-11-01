import sys
input = sys.stdin.readline


k, n = map(int, input().split())
k_lst = []
for _ in range(k):
    k_lst.append(int(input()))
k_lst.sort()

start, end = 1, k_lst[-1]
while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in k_lst:
        x = i // mid
        count += x

    if count >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)

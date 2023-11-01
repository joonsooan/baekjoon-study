import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
lst.sort()

if sum(lst) <= m:           # If total budget is smaller than m
    print(lst[-1])
else:
    start, end = 0, lst[-1]

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in range(n):  # Calculating total sum of budget
            if lst[i] <= mid:
                total += lst[i]
            else:
                total += mid

        if total > m:
            end = mid - 1
        else:
            start = mid + 1
    print(end)

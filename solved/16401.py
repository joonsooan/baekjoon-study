m, n = map(int, input().split())
lst = list(map(int, input().split()))
start, end = 1, max(lst)

if sum(lst) < m:
    print(0)
else:
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        for i in lst:
            if i >= mid:
                cnt += i // mid

        if cnt >= m:
            start = mid + 1
        else:
            end = mid - 1

    print(end)

n, m = map(int, input().split())
lst = list(map(int, input().split()))
# 'start' must be max(lst), because one video can't be longer than one blueray
start, end = max(lst), sum(lst)

while start <= end:
    mid = (start + end) // 2
    total = 0
    cnt = 0

    # Calculating how many bluerays are used
    for i in lst:
        if total + i > mid:
            cnt += 1
            total = 0
        total += i

    # Remaining value = One blueray
    if total != 0:
        cnt += 1

    # Fewer bluerays used -> mid is too big
    # If cnt = m -> We can still find minimum mid value
    if cnt <= m:
        end = mid - 1
    # Too many bluerays used -> mid is too small
    else:
        start = mid + 1

print(start)

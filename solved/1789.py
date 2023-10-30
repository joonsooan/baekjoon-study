s = int(input())
start, end = 1, s

while start <= end:
    mid = (start + end) // 2
    if (mid * (mid+1)) // 2 <= s:
        start = mid + 1
    else:
        end = mid - 1

print(end)

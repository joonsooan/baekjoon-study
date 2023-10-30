import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    log = 0
    # print(f"mid: {mid}")

    for tree in trees:
        if tree >= mid:
            log += tree - mid

    if log >= m:
        # print("too long")
        start = mid + 1
    else:
        # print("too short")
        end = mid - 1
    # print(f"start: {start}, end: {end}")
    # print()

print(end)

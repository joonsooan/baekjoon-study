import sys
input = sys.stdin.readline

n, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
start, end = 1, lst[-1] - lst[0]

# 가장 인접한 공유기 사이의 최대 거리를 이분탐색으로 결정
while start <= end:
    mid = (start + end) // 2
    # 첫 번째 공유기는 첫 번째 집으로 확정
    cnt = 1
    curr = lst[0]  # curr의 위치마다 공유기 설치

    for i in range(1, n):
        if lst[i] - curr >= mid:
            cnt += 1
            curr = lst[i]

    if cnt >= c:
        start = mid + 1
    else:
        end = mid - 1

print(end)

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()
start, end = 1, lst[-1] - lst[0]
res = 0

if c == 2:
    print(lst[-1] - lst[0])
else:
    while start < end:
        mid = (start + end) // 2
        count = 1
        last_router = lst[0]  # 마지막 공유기 위치

        for i in range(n):
            if lst[i] - last_router >= mid:  # 집 간격이 mid보다 큰 경우
                count += 1                   # 공유기 개수 + 1
                last_router = lst[i]         # 마지막 공유기 위치 업데이트

        if count >= c:        # 공유기 개수가 c보다 큰 경우
            res = mid         # 정답: 현재 mid 값
            start = mid + 1   # 더 큰 mid가 있을 수 있기에 큰 범위로 업데이트
        else:                 # 공유기 개수가 c보다 작은 경우
            end = mid         # 작은 범위로 업데이트
    print(res)

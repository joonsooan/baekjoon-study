n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    max_idx = i

    # 큰 수가 없는 경우
    if max_idx == i:
        print(-1)

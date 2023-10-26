n = int(input())
lst = list(map(int, input().split()))

for i in range(n-1, 0, -1):          # 맨 뒤 값부터 탐색
    if lst[i-1] < lst[i]:            # 오름차순이 끊기면
        for j in range(n-1, 0, -1):  # 다시 맨 뒤 값부터 탐색
            if lst[i-1] < lst[j]:    # 끊긴 값보다 큰 값을 찾으면
                lst[i-1], lst[j] = lst[j], lst[i-1]  # 두 개의 값을 교환
                lst = lst[:i] + sorted(lst[i:])      # 바뀐 값을 기준으로 뒤의 배열을 정렬
                for i in lst:
                    print(i, end=' ')
                exit()
print(-1)

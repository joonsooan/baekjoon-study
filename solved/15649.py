def dfs():
    if len(s) == m:  # 리스트 안에 m개의 요소가 쌓이면 출력
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if visited[i]:  # 처음엔 False
            continue
        visited[i] = True  # True로 바꿈
        s.append(i)  # s 리스트에 추가
        dfs()  # 함수를 다시 실행 -> 다음 자리수로 이동
        s.pop()
        visited[i] = False


n, m = map(int, input().split())
s = []
visited = [False] * (n + 1)

dfs()

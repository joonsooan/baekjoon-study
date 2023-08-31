def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        s.append(i)  # 중복도 허용이므로 그대로 추가
        dfs()  # 오름차순으로 정렬해야 하므로 i + 1
        s.pop()  # return을 하고 맨 뒤의 요소를 제거


n, m = map(int, input().split())
s = []
dfs()

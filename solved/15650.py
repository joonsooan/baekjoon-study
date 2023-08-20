def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        if i not in s:  # 리스트에 i가 없으면 삽입
            s.append(i)
            dfs(i + 1)  # 오름차순으로 정렬해야 하므로 i + 1
            s.pop()  # return을 하고 맨 뒤의 요소를 제거


n, m = map(int, input().split())
s = []
dfs(1)

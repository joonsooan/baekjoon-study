def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n):
        s.append(num_list[i])
        dfs(i)  # 비내림차순 정렬이므로 i로 인자를 전달
        s.pop()  # return을 하고 맨 뒤의 요소를 제거


n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

s = []
dfs(0)

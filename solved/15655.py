def dfs(start):  # 파라미터를 시작 인덱스로 설정
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n):
        if num_list[i] not in s:
            s.append(num_list[i])
            dfs(i + 1)
            s.pop()


n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

s = []
dfs(0)

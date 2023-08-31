def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(0, n):
        s.append(num_list[i])  # 중복도 허용이므로 그대로 추가
        dfs()  # 오름차순으로 정렬해야 하므로 i + 1
        s.pop()  # return을 하고 맨 뒤의 요소를 제거


n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

s = []
dfs()

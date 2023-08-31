def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for num in num_list:
        if num not in s:
            s.append(num)
            dfs()
            s.pop()


n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

s = []
dfs()

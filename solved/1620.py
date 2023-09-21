import sys

n, m = map(int, sys.stdin.readline().split())
poke_dict = {}
poke_lst = []

for i in range(1, n + 1):
    poke_name = sys.stdin.readline().strip()
    poke_dict[poke_name] = i
    poke_lst.append(poke_name)

for i in range(m):
    x = sys.stdin.readline().strip()
    if x.isdigit():  # 번호인 경우
        x = int(x)
        print(poke_lst[x-1])
    else:  # 이름인 경우
        print(poke_dict[x])

import sys

n, m = map(int, sys.stdin.readline().split())

never_heard_dict = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    never_heard_dict[name] = 1

never_seen_dict = {}
for i in range(m):
    name = sys.stdin.readline().strip()
    never_seen_dict[name] = 1

result = 0
result_lst = []
for name in never_heard_dict:
    if never_seen_dict.get(name) == 1:
        result += 1
        result_lst.append(name)

result_lst.sort()
print(result)
for name in result_lst:
    print(name)

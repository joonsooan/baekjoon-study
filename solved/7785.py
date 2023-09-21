import sys

n = int(sys.stdin.readline())
log_dict = {}
log_lst = []

for i in range(n):
    name, log = map(str, sys.stdin.readline().split())
    if log == "enter":
        log_dict[name] = 1
    elif log == "leave":
        log_dict[name] = 0

for key in log_dict.keys():
    if log_dict[key] == 1:  # 시간복잡도: O(1)
        log_lst.append(key)

log_lst.sort(reverse=True)
for name in log_lst:
    print(name)

from collections import deque

n = int(input())
a = list(map(int, input().split()))

result = [-1] * n
f_dict = {}
stk = deque()

for i in range(n):
    if a[i] in f_dict:
        f_dict[a[i]] += 1
    else:
        f_dict[a[i]] = 1

for i in range(n):
    while stk and (f_dict[stk[-1][0]] < f_dict[a[i]]):
        tmp, idx = stk.pop()
        result[idx] = a[i]
    stk.append([a[i], i])

print(*result)

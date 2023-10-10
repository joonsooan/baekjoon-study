from collections import deque

n = int(input())
a = list(map(int, input().split()))

result = [-1] * n
stk = deque()

for i in range(n):
    while stk and (stk[-1][0] < a[i]):
        tmp, idx = stk.pop()
        result[idx] = a[i]
    stk.append([a[i], i])

print(*result)

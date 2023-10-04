import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque(enumerate(map(int, sys.stdin.readline().split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, ans)))

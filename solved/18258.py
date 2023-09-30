import sys
from collections import deque
n = int(sys.stdin.readline())
deq = deque()

for i in range(n):
    order_lst = list(map(str, sys.stdin.readline().split()))
    order = order_lst[0]

    if order == "push":
        deq.append(order_lst[1])
    elif order == "pop":
        if len(deq) != 0:
            print(deq[0])
            deq.popleft()
        else:
            print(-1)
    elif order == "size":
        print(len(deq))
    elif order == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)
    elif order == "back":
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)

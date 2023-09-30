import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque()
for i in range(n):
    order_lst = list(map(int, sys.stdin.readline().split()))
    order = order_lst[0]

    if order == 1:
        deq.appendleft(order_lst[1])
    elif order == 2:
        deq.append(order_lst[1])
    elif order == 3:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif order == 4:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif order == 5:
        print(len(deq))
    elif order == 6:
        if deq:
            print(0)
        else:
            print(1)
    elif order == 7:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif order == 8:
        if deq:
            print(deq[-1])
        else:
            print(-1)

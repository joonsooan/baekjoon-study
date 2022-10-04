import sys
from collections import deque

num_of_commands = int(sys.stdin.readline())
deq = deque()

for i in range(num_of_commands):
    commmand_list = sys.stdin.readline().split()
    command = commmand_list[0]

    if len(commmand_list) > 1:
        number = commmand_list[1]

    if command == "push_front":
        deq.appendleft(number)

    elif command == "push_back":
        deq.append(number)

    elif command == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())

    elif command == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())

    elif command == "size":
        print(len(deq))

    elif command == "empty":
        if len(deq) == 0:
            print(1)
        else:
            print(0)

    elif command == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])

    elif command == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
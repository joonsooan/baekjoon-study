import sys

num_of_commands = int(sys.stdin.readline())
queue = []

for i in range(num_of_commands):
    commmand_list = sys.stdin.readline().split()
    command = commmand_list[0]

    if len(commmand_list) > 1:
        number = commmand_list[1]

    if command == "push":
        queue.append(number)

    elif command == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            removed = queue.pop(0)
            print(removed)

    elif command == "size":
        print(len(queue))

    elif command == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif command == "back":
        if len(queue) == 0:
            print(-1)
        else:
            end_num = len(queue) - 1
            print(queue[end_num])

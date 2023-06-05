import sys

num_of_commands = int(sys.stdin.readline())
stack = []

for i in range(num_of_commands):
    commmand_list = sys.stdin.readline().split()
    command = commmand_list[0]

    if len(commmand_list) > 1:
        number = commmand_list[1]

    if command == "push":
        stack.append(number)

    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            end_num = len(stack) - 1
            removed = stack.pop(end_num)
            print(removed)

    elif command == "size":
        print(len(stack))

    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            end_num = len(stack) - 1
            print(stack[end_num])

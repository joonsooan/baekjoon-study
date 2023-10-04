import sys

stk_1 = list(sys.stdin.readline().rstrip())
stk_2 = []
m = int(sys.stdin.readline())

for i in range(m):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'L':
        if stk_1:
            stk_2.append(stk_1.pop())

    elif command[0] == 'D':
        if stk_2:
            stk_1.append(stk_2.pop())

    elif command[0] == 'B':
        if stk_1:
            stk_1.pop()

    else:
        stk_1.append(command[1])

stk_1.extend(reversed(stk_2))
print(''.join(stk_1))

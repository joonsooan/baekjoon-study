import sys


def push(n):
    stack.append(n)


def pop():
    if len(stack) > 0:
        print(stack[-1])
        stack.pop()
    else:
        print(-1)


def length():
    print(len(stack))


def is_empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def peek():
    if len(stack) > 0:
        print(stack[-1])
    else:
        print(-1)


stack = []
n = int(sys.stdin.readline())
for i in range(n):
    lst = list(map(int, sys.stdin.readline().split()))

    if len(lst) == 2:
        push(lst[1])
    else:
        n = lst[0]
        if n == 2:
            pop()
        elif n == 3:
            length()
        elif n == 4:
            is_empty()
        elif n == 5:
            peek()

import sys
input = sys.stdin.readline

m = int(input())
bit = 0

for _ in range(m):
    order = input().split()

    if order[0] == 'all':
        bit = (1 << 20) - 1
    elif order[0] == 'empty':
        bit = 0
    else:
        op = order[0]
        num = int(order[1]) - 1

        if op == 'add':
            bit |= (1 << num)
        elif op == 'remove':
            bit &= ~(1 << num)
        elif op == 'check':
            if bit & (1 << num) == 0:  # S에 x가 없는 경우
                print(0)
            else:
                print(1)
        elif op == 'toggle':  # S에 x가 있으면 제거, 없으면 추가
            bit ^= (1 << num)

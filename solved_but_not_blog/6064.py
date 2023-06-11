import sys


def calcuclate(m, n, x, y):
    while x <= m * n:  # m * n은 마지막 해
        if (x - y) % n == 0:
            return x
        x += m  # x에 m을 계속 더한 값이 y에 n을 더한 값과 같을 때
    return -1  # 다 돌았는데 나오지 않으면 -1을 반환


T = int(input())

for i in range(T):
    m, n, x, y = map(int, sys.stdin.readline().split())

    print(calcuclate(m, n, x, y))

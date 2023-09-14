import sys

a1, a0 = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
n0 = int(sys.stdin.readline())

if c < a1:  # f(n)이 c x g(n)을 추월하는 순간이 반드시 있음
    print(0)

elif c == a1:  # n의 계수가 같은 경우
    if a0 <= n0:  # n의 최솟값인 n0보다 작거나 같으면
        print(1)
    else:         # n0보다 크면 반례가 존재
        print(0)

else:  # c > a1
    if n0 >= a0 / (c - a1):
        print(1)
    else:  # 반례가 되는 n이 존재
        print(0)

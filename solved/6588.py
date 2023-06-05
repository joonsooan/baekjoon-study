import sys

MAX_NUM = 1000000


def Goldbach():
    num_list = [False, False] + [True] * MAX_NUM  # 0과 1은 예외처리

    for i in range(2, 1001):
        if num_list[i] == True:
            for j in range(i + i, MAX_NUM + 1, i):
                num_list[j] = False
    # 에라토스테네스의 체 이용

    while True:
        n = int(sys.stdin.readline())
        if n == 0:  # 0인 경우 종료
            break
        for i in range(3, len(num_list)):  # 홀수인 두 소수의 합이므로 3부터 시작
            if num_list[i] and num_list[n - i]:  # i + (n - i) = n
                print(f"{n} = {i} + {n - i}")
                break


Goldbach()

import sys


def prime_list(first_num, last_num):
    sieve = [True] * (last_num + 1)
    sieve[1] = False  # 1은 예외처리

    m = int(last_num**0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:  # 소수인 경우
            for j in range(i + i, last_num + 1, i):
                sieve[j] = False  # n까지 소수의 배수들을 모두 없앰.
    # print(sieve)
    return [i for i in range(first_num, last_num + 1) if sieve[i] == True]  # 소수를 반환


M, N = map(int, sys.stdin.readline().split())
list = prime_list(M, N)
for i in list:
    print(i)

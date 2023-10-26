# Top-Down 방식

memoization = [0] * 100  # 값을 저장해놓을 리스트 생성


def fibo(x):
    if x == 1 or x == 2:
        return 1
    elif memoization[x] != 0:
        return memoization[x]
    memoization[x] = fibo(x - 1) + fibo(x - 2)
    return memoization[x]


print(fibo(99))


# Bottom-Up 방식

dp = [0] * 100  # DP 테이블 초기화
dp[1] = 1
dp[2] = 1
n = 99  # n까지의 피보나치 합을 구함

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])

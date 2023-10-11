# 오래 걸리는 코드
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result


# n, m = map(int, input().split())
# num = factorial(n) // (factorial(m) * factorial(n - m))
# num = list(str(num))
# ans = 0

# for i in range(len(num)):
#     if num.pop() == '0':
#         ans += 1
#     else:
#         break
# print(ans)

# 소인수분해를 해서 2와 5의 개수를 구하기
def find_two(n):
    two = 0
    while n != 0:
        n = n // 2
        two += n
    return two


def find_five(n):
    five = 0
    while n != 0:
        n = n // 2
        five += n
    return five


n, m = map(int, input().split())
num_two = find_two(n) - find_two(m) - find_two(n-m)
num_five = find_five(n) - find_five(m) - find_five(n-m)
print(min(num_two, num_five))

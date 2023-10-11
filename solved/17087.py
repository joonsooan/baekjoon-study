import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n, s = map(int, sys.stdin.readline().split())
p_lst = list(map(int, sys.stdin.readline().split()))
dis_lst = []

# 수빈이와 동생들 사이의 거리
for p in p_lst:
    x, y = max(s, p), min(s, p)
    dis_lst.append(x - y)
# print(dis_lst)

res = dis_lst[0]
for i in range(1, n):
    res = gcd(dis_lst[i], res)
print(res)

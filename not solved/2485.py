import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(sys.stdin.readline())
tree_lst = []
for i in range(n):
    tree_lst.append(int(sys.stdin.readline()))

gap_lst = []
for i in range(n-1):
    gap = tree_lst[i+1] - tree_lst[i]
    gap_lst.append(gap)

min_gcd = gap_lst[0]
result = 0

for i in range(n-2):
    temp_gcd = gcd(gap_lst[i], gap_lst[i+1])

    if temp_gcd == 1:
        result = sum(gap_lst) - len(gap_lst)
        print(result)
        break
    else:
        if temp_gcd < min_gcd:
            min_gcd = temp_gcd

    if i == n-3:  # 마지막 케이스에서 오류...?
        for gap in gap_lst:
            result += (gap // min_gcd) - 1
        print(result)

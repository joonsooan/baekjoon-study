import sys
input = sys.stdin.readline


def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)


n = int(input())
if n == 0:
    print(0)
else:
    lst = [int(input()) for _ in range(n)]
    lst.sort()
    bound = round2(n * 0.15)
    total, average = 0, 0

    for i in range(bound, n-bound):
        total += lst[i]

    average = round2(total/(n-(2*bound)))
    print(average)

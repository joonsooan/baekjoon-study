import sys


def binary_search(lst, target):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if target < lst[mid]:
            end = mid - 1
        elif target > lst[mid]:
            start = mid + 1
        else:
            return 1
    return 0


input = sys.stdin.readline
n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
m = int(input())
m_lst = list(map(int, input().split()))

for i in m_lst:
    print(binary_search(n_lst, i))

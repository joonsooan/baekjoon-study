import sys


def cal_max_score(first_row, sec_row):
    pass


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    first_row = list(map(int, sys.stdin.readline().split()))
    sec_row = list(map(int, sys.stdin.readline().split()))
    cal_max_score(first_row, sec_row)

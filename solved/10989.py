import sys

n = int(sys.stdin.readline())
lst = [0 for _ in range(10001)]  # 카운팅 정렬

for i in range(n):
    num = int(sys.stdin.readline())
    lst[num] += 1

for idx, val in enumerate(lst):
    if val != 0:  # 카운팅된 수인 경우
        for j in range(val):  # 카운팅된 횟수만큼
            print(idx)  # 해당 수를 출력

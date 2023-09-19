import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y])

lst.sort(key=lambda x: x[0])  # 먼저 x좌표 오름차순으로 정렬
lst.sort(key=lambda x: x[1])  # 다음 y좌표 오름차순으로 정렬

for x, y in lst:
    print(f"{x} {y}")

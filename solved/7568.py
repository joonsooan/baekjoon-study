import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    cnt = 1
    for j in range(n):
        if j == i:
            pass
        elif lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    print(cnt, end=' ')

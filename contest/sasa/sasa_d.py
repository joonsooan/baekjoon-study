import sys
input = sys.stdin.readline

#
n, m = map(int, input().split())
h, w = map(int, input().split())
cw_lst = []
for i in range(n):
    cw_lst.append(list(map(int, input().split())))
k = int(input())
for i in range(k):
    sewer_loc = list(map(int, input().split()))
    cw_lst[sewer_loc[0]-1][sewer_loc[1]-1] = 0
#
# print(cw_lst)
for i in range(n):
    for j in range(m):
        loc = cw_lst[i][j]
while True:
    flag = True
    for i in range(n):
        for j in range(m):
            loc = cw_lst[i][j]
            if loc == 0:  # 하수구인 경우 다음 위치로 이동
                flag = False
                break
            else:
                if i-1 >= 0:
                    if j-1 >= 0:
                        pass
        if flag == False:
            break

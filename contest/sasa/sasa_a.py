import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().rstrip().split()))
q = int(input())
query_lst = []
for i in range(q):
    query_lst.append(list(map(int, input().rstrip().split())))

for i in range(q):
    order = query_lst[i][0]
    if order == 1:
        l, r, k = query_lst[i][1], query_lst[i][2], query_lst[i][3]
        total = 0
        for j in range(l-1, r):
            if lst[j] == k:
                total += 1
        print(total)
    else:
        l, r = query_lst[i][1], query_lst[i][2]
        for j in range(l-1, r):
            lst[j] = 0

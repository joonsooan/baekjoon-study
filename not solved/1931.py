import sys
input = sys.stdin.readline

n = int(input())
lst = [[0, 0] for _ in range(n)]
for i in range(n):
    s, e = map(int, input().split())
    lst[i][0] = s
    lst[i][1] = e

new_lst = lst
print(sorted(new_lst))
lst.sort(key=lambda x: x[1])
print(lst)
lst.sort(key=lambda x: x[0])
print(lst)

# cnt = 1
# end_time = lst[0][1]
# for i in range(1, n):
#     if lst[i][0] >= end_time:
#         cnt += 1
#         end_time = lst[i][1]

# print(cnt)

import sys
input = sys.stdin.readline


def round2(num):
    abs_num = abs(num)
    if num >= 0:
        return int(abs_num) + (1 if abs_num - int(abs_num) >= 0.5 else 0)
    else:
        return -(int(abs_num) + (1 if abs_num - int(abs_num) >= 0.5 else 0))


n = int(input())
lst = [int(input()) for _ in range(n)]

num_dict = {}
lst.sort()
total = sum(lst)
average = round2(total / n)

# 산술평균
print(average)
# 중앙값
print(lst[n//2])

for i in lst:
    if i in num_dict:
        num_dict[i] += 1
    else:
        num_dict[i] = 1

max_val = max(num_dict.values())
key_lst = []
for key in num_dict.keys():
    if num_dict[key] == max_val:
        key_lst.append(key)

# 최빈값
list(set(key_lst)).sort()
if len(key_lst) == 1:
    print(key_lst[0])
else:
    print(key_lst[1])

# 범위
print(max(num_dict.keys()) - min(num_dict.keys()))

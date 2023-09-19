lst = list(input())
n_lst = [int(x) for x in lst]
n_lst.sort(reverse=True)

result = 0
ten = 1
for i in range(len(n_lst), 0, -1):
    result += n_lst[i-1] * ten
    ten *= 10

print(result)

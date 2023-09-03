array = []
for i in range(9):
    array.append(list(map(int, input().split())))

max_num = 0
max_index_i = 0
max_index_j = 0

for i in range(9):
    for j in range(9):
        if array[i][j] >= max_num:
            max_num = array[i][j]
            max_index_i = i + 1
            max_index_j = j + 1

print(max_num)
print(max_index_i, max_index_j)

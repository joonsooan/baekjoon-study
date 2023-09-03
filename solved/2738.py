n, m = map(int, input().split())
a_array = []
b_array = []

for i in range(n):
    a_array.append(list(map(int, input().split())))

for i in range(n):
    b_array.append(list(map(int, input().split())))

answer_array = a_array

for i in range(n):
    for j in range(m):
        answer_array[i][j] = a_array[i][j] + b_array[i][j]

for i in range(n):
    for j in range(m):
        print(answer_array[i][j], end=' ')
    print("")

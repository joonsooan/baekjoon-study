numbers = input().split()
N = int(numbers[0])
K = int(numbers[1])
list = []
permutation = []

for i in range(N):
    list.append(i + 1)

next_index = (list.index(K) + K)
adding_num = list.pop(list.index(K))

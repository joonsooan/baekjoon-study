# array = []

# for i in range(5):
#     input_list = list(input())
#     if len(input_list) < 15:  # 15개로 안 채워진 경우 -1을 대신 대입
#         for j in range(15 - len(input_list)):
#             input_list.append(-1)
#     array.append(input_list)

# answer = ""
# for i in range(15):
#     for j in range(5):
#         if array[j][i] == -1:  # 요소가 -1인 경우 무시하고 넘어감
#             continue
#         answer += array[j][i]

# print(answer)


words = [input() for i in range(5)]
print(words)

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')

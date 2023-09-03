import sys

n = int(input())
answer = 0

for i in range(n):
    s = sys.stdin.readline()
    char_dict = {}
    temp = ""
    for char in s:
        prev = temp
        temp = char
        if char not in char_dict:
            char_dict[char] = 0
        elif char in char_dict and prev == temp:
            char_dict[char] = 1
        elif char in char_dict and prev != temp:
            char_dict[char] = -1
            break  # 그룹이 아닐 경우 바로 반복문 탈출

    if -1 not in char_dict.values():
        answer += 1

# answer = n

# for i in range(n):
#     word = input()
#     for j in range(0, len(word)-1):
#         if word[j] == word[j+1]:  # 해당 인덱스와 다음 인덱스의 문자가 같으면 패스
#             pass
#         elif word[j] in word[j+1:]:  # 해당 인덱스와 다음 인덱스의 문자가 다르고, 해당 인덱스의 문자가 뒤의 문자열에 포함되어 있는 경우 그룹이 아님
#             answer -= 1
#             break

# print(answer)

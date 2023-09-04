# from string import ascii_uppercase

# j = 0
# for i in ascii_uppercase:
#     alphabet_dict[i] = j + 10
#     j += 1
# print(alphabet_dict)

# alphabet_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13,
#                  'E': 14, 'F': 15, 'G': 16, 'H': 17,
#                  'I': 18, 'J': 19, 'K': 20, 'L': 21,
#                  'M': 22, 'N': 23, 'O': 24, 'P': 25,
#                  'Q': 26, 'R': 27, 'S': 28, 'T': 29,
#                  'U': 30, 'V': 31, 'W': 32, 'X': 33,
#                  'Y': 34, 'Z': 35}
# num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# n, b = map(str, input().split())  # n: 숫자, b: 진법
# b = int(b)  # b를 정수로 변환

# result = 0
# power = len(n) - 1  # 지수를 나타내는 변수

# for c in n:
#     # print(c)
#     if c in num_list:  # c가 숫자인 경우
#         c = int(c)  # 정수로 변환
#         result += c * (b ** power)
#     elif c in alphabet_dict:  # c가 문자인 경우
#         result += alphabet_dict[c] * (b ** power)
#     power -= 1

# print(result)

N, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # A의 인덱스는 10, B는 11, ...

N = N[::-1]  # 입력받은 N을 자리수가 낮은 순으로 슬라이싱
result = 0

for i, n in enumerate(N):
    result += (int(b)**i) * (ary.index(n))  # b를 i제곱하고 숫자 혹은 문자에 해당하는 값을 곱함
print(result)

# s = input()
# prev = '('
# stick = 0
# num_lazer = 0
# num_left = 0
# result = 0

# for c in s:
#     if prev == '(':
#         if c == '(':    # ( or ((
#             stick += 1
#             num_left += 1
#         else:           # ()
#             prev = ')'
#             stick -= 1
#             num_lazer += 1
#             result += stick

#     else:  # prev == ')'
#         if c == '(':    # )(
#             prev = '('
#             stick += 1
#             num_left += 1
#         else:           # ))
#             stick -= 1

# num_stick = num_left - num_lazer
# print(result + num_stick)

s = input()
stk = []
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stk.append('(')
    else:  # ')'
        if s[i-1] == '(':    # ()
            stk.pop()
            cnt += len(stk)  # 현재 쇠막대기 개수만큼 카운트

        else:                # ))
            stk.pop()        # 막대기 하나 끝
            cnt += 1         # 잘리고 남은 부분 카운트

print(cnt)

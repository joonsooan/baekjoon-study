s = input()
a = list('abcdefghijklmnopqrstuvwxyz')
a_13 = list('nopqrstuvwxyzabcdefghijklm')
a_dict = {x: i for i, x in enumerate(a)}
result = ''

for c in s:
    if c.isalpha():      # 문자인 경우
        if c.isupper():  # 대문자인 경우
            result += a_13[a_dict[c.lower()]].upper()
        else:            # 소문자인 경우
            result += a_13[a_dict[c]]
    else:                # 숫자 / 공백인 경우
        result += c

print(result)

# 아스키 코드를 이용한 풀이
n = input()
res = ''
for i in range(len(n)):
    if n[i] == ' ' or ord(n[i]) < ord('A'):
        res += n[i]
    else:
        if ord(n[i]) + 13 > 122:                      # 소문자인 경우 (일부)
            res += chr(96 + (ord(n[i]) + 13) - 122)
        elif ord(n[i]) + 13 > 90 and ord(n[i]) < 91:  # 대문자인 경우 (일부)
            res += chr(64 + (ord(n[i]) + 13) - 90)
        else:                                         # 대소문자 남은 경우
            res += chr(ord(n[i]) + 13)
print(res)

s = list(input())
stk = []
ans = []
is_tag = False

for c in s:
    if is_tag:
        ans.append(c)
        if c == '>':
            is_tag = False

    else:  # tag 밖에 있을 때
        if c == ' ':
            while stk:
                ans.append(stk.pop())
            ans.append(' ')
        elif c == '<':
            while stk:
                ans.append(stk.pop())
            is_tag = True
            ans.append('<')
        else:  # 숫자나 문자인 경우
            stk.append(c)

while stk:  # stk 안에 남은 문자 출력
    ans.append(stk.pop())

print(''.join(ans))

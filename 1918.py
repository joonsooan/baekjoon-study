s = input()
operand_stk = []   # 피연산자 스택
operator_stk = []  # 연산자 스택

for i in range(len(s)):
    if s[i] == '(' or s[i] == ')':      # 괄호인 경우
        pass
    elif s[i] in ['+', '-', '*', '/']:  # 연산자인 경우
        pass
    else:                               # 피연산자인 경우
        pass

print(operand_stk.pop())

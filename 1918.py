s = input()
operand_stk = []   # 피연산자 스택
operator_stk = []  # 연산자 스택

for i in range(len(s)):
    curr = s[i]

    if curr in ['+', '-', '*', '/']:  # 연산자인 경우
        operator_stk.append(curr)
    elif operator_stk:                # 피연산자가 들어왔고 연산자가 존재할 때
        tmp = operand_stk.pop() + curr + operator_stk.pop()
        operand_stk.append(tmp)
    else:                             # 피연산자인 경우
        operand_stk.append(s[i])

    print(operand_stk)
    print(operator_stk)

# 마지막 정답 출력
print(operand_stk.pop())


# 고쳐야 할 부분
# 1. 곱셈/나눗셈, 덧셈/뺄셈 우선순위 두기
# 2. 괄호를 만났을 때 연산 추가하기

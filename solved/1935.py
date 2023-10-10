import sys

n = int(sys.stdin.readline())
s_lst = list(sys.stdin.readline().rstrip())
s_dict = {key: 0 for key in s_lst if key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
stk = []

# 피연산자에 대응하는 수 저장
for key in s_dict:
    s_dict[key] = int(sys.stdin.readline())

for s in s_lst:
    if s in ['+', '-', '*', '/']:  # 연산자가 온 경우
        operator = s
        tmp_2 = stk.pop()
        tmp_1 = stk.pop()
        if operator == '+':
            cal = tmp_1 + tmp_2
        elif operator == '-':
            cal = tmp_1 - tmp_2
        elif operator == '*':
            cal = tmp_1 * tmp_2
        else:
            cal = tmp_1 / tmp_2
        stk.append(cal)
    else:                # 피연산자가 온 경우
        val = s_dict[s]  # 피연산자에 대응하는 수
        stk.append(val)  # 스택에 추가

print(f"{stk.pop():.2f}")

import sys

n = int(sys.stdin.readline())
stk = []
ans = []
flag = 0
cur = 1

for i in range(n):
    num = int(sys.stdin.readline())
    while cur <= num:    # 입력한 수를 만날 때까지 오름차순으로 push
        stk.append(cur)  # 반복했을 때 cur > num인 경우 while문 무시
        ans.append("+")
        cur += 1

    if stk[-1] == num:   # stk의 top이 입력한 숫자와 같다면
        stk.pop()        # 스택의 top을 pop
        ans.append("-")
    else:                # num이 top보다 작으면 불가능
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in ans:
        print(i)

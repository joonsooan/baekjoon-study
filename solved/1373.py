n = input()[::-1]
ans = []
tmp = 0		# 각 자릿수의 계산 결과를 담을 변수
cnt = 1		# 곱해줄 배수 : 1, 2, 4

for i in n:
    if cnt < 8:
        tmp += cnt * int(i)
        cnt *= 2
    else:
        ans.append(str(tmp))
        tmp = 1 * int(i)  # cnt = 1
        cnt = 2
ans.append(str(tmp))
for _ in range(len(ans)):
    print(str(ans.pop()), end='')

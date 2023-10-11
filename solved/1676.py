factorial = 1
for i in range(1, int(input()) + 1):
    factorial *= i
factorial = list(str(factorial))
ans = 0

for i in range(len(factorial)):
    if factorial.pop() == '0':
        ans += 1
    else:
        break
print(ans)

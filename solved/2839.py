import sys


n = int(sys.stdin.readline())

lst = []
three_quotient = n // 3
five_quotient = n // 5
possible = False

for i in range(three_quotient + 1):
    for j in range(five_quotient + 1):
        if 3*i + 5*j == n:
            lst.append(i + j)
            possible = True

if not possible:
    print(-1)
else:
    print(min(lst))

n = int(input())
add = 0

if n == 1:
    print(9)
else:
    for i in range(1, n):
        add += 2 ** i
    print((3 + add)**2)

n = int(input())

for i in range(1, n+1):
    blank = " " * (n - i)
    star = "*" * (2 * i - 1)
    print(f"{blank}{star}")

for i in range(1, n):
    blank = " " * i
    star = "*" * (2 * (n - i) - 1)
    print(f"{blank}{star}")

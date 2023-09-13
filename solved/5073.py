import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0:
        break

    max_num = max(a, b, c)
    if max_num * 2 >= (a + b + c):
        print("Invalid")
    elif a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")

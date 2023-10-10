import sys

while True:
    line = sys.stdin.readline().rstrip('\n')
    if not line:
        break
    l, u, d, s = 0, 0, 0, 0

    for c in line:
        if c.islower():
            l += 1
        elif c.isupper():
            u += 1
        elif c.isdigit():
            d += 1
        elif c.isspace():
            s += 1

    print(l, u, d, s)

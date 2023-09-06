t = int(input())

for i in range(t):
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    c = int(input())

    while True:
        if c >= 25:
            quarter += c // 25
            c %= 25
        elif c >= 10:
            dime += c // 10
            c %= 10
        elif c >= 5:
            nickel += c // 5
            c %= 5
        elif c >= 1:
            penny += c
            break
        else:
            break

    print(f"{quarter} {dime} {nickel} {penny}")

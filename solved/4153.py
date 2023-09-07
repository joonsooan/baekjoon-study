while True:
    a, b, c = map(int, input().split())
    if a == 0:  # 0 0 0이 입력된 경우
        break

    sides = [a, b, c]
    sides.sort()
    if sides[2]**2 == (sides[0]**2) + (sides[1]**2):
        print("right")
    else:
        print("wrong")

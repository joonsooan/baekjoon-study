n = list(input())
res = []

power = 0
num = 0
while True:
    if not n:  # 리스트에 요소가 없으면 break
        break
    if power != 3:
        print(f"power: {power}")
        if n.pop() == '1':
            num += 2**power
        power += 1
        print(num)
    else:  # power = 3일 때
        print(f"append: {num}")
        res.append(num)
        power = 0
        num = 0
    print(f"n: {n}")
    print("##########################3")

print(res)

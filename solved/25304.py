paid_money = int(input())
num_of_kind = int(input())
total = 0

for i in range(num_of_kind):
    a, b = map(int, input().split())
    total += a * b

if paid_money == total:
    print("Yes")
else:
    print("No")
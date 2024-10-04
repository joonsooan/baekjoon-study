n = int(input())
shirt_lst = list(map(int, input().split()))
t, p = map(int, input().split())
total_shirt = 0

for shirt in shirt_lst:
    x = shirt // t
    if shirt % t == 0:
        total_shirt += x
    else:
        total_shirt += (x + 1)

print(total_shirt)
print(n // p, n % p)

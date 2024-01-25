import sys
input = sys.stdin.readline

n, k = map(int, input().split())
count = 0
lst = []
for i in range(n):
    lst.append(int(input()))
coins = lst[::-1]

for coin in coins:
    if k >= coin:
        count += k // coin
        k %= coin
        if k == 0:
            break
print(count)

n, m = map(int, input().split())
baskets = [i for i in range(1, n+1)]

for l in range(m):
    i, j = map(int, input().split())
    while True:
        baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]
        i += 1
        j -= 1
        if i >= j:
            break

for num in baskets:
    print(num, end=' ')

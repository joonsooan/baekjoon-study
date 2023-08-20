N = int(input())
calculate = True
i = 1
sum = 0

while calculate:
    if N // 10**i >= 1:
        sum += i * (10 ** (i - 1)) * 9
        i += 1
    else:
        sum += i * (N - 10 ** (i - 1) + 1)
        calculate = False

print(sum)

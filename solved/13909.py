n = int(input())
i = 1
result = 0

while True:
    if i**2 <= n:
        result += 1
        i += 1
    else:
        break
print(result)

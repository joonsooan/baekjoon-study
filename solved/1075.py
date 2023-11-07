n = int(input())
f = int(input())
last_two = n % 100
n -= last_two
i = 0

while True:
    if n % f == 0:
        print(str(i).zfill(2))
        break
    i += 1
    n += 1

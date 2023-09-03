list = [i for i in range(1, 31)]

for i in range(28):
    n = int(input())
    list.remove(n)

for n in list:
    print(n)

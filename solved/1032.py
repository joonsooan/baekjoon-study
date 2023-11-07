n = int(input())
lst = []
for _ in range(n):
    x = input()
    if not lst:
        lst = list(x)
    else:
        x = list(x)
        for i in range(len(lst)):
            if lst[i] == '?':
                pass
            elif lst[i] != x[i]:
                lst[i] = '?'

print(''.join(lst))

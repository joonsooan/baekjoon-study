def fact(n):
    if n == 0:
        return 1
    elif n > 1:
        return n * fact(n - 1)
    else:
        return n


N = int(input())
print(fact(N))

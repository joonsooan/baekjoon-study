def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n_lst = []
d_lst = []

for i in range(2):
    n, m = map(int, input().split())
    n_lst.append(n)
    d_lst.append(m)

numerator = (n_lst[0] * d_lst[1]) + (n_lst[1] * d_lst[0])
denominator = d_lst[0] * d_lst[1]

gcd = gcd(numerator, denominator)
if gcd == 1:
    print(f"{numerator} {denominator}")
else:
    print(f"{numerator // gcd} {denominator // gcd}")
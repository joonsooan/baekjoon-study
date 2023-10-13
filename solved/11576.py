def convert_base(n, q):  # n: 변환할 수, q: 몇 진법인지
    rev_base = []

    while n > 0:
        n, mod = divmod(n, q)       # 몫, 나머지
        rev_base.append(str(mod))   # 나머지를 더해줌

    return rev_base[::-1]


# 변수 입력
a, b = map(int, input().split())
m = int(input())
lst = list(map(int, input().split()))
num = 0
cnt = 1

# a진법 숫자를 10진수로 변환
for i in range(len(lst)):
    num += (lst.pop()) * cnt
    cnt *= a

# 10진수로 변환한 수를 b진법으로 변환
ans = convert_base(num, b)
print(' '.join(ans))

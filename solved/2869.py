a, b, v = map(int, input().split())
height = 0
days = 0

while True:
    height += a
    days += 1
    if height >= v:
        print(days)
        break
    height -= b

# 이렇게 하면 시간이 너무 오래 걸리는 경우 존재
# 시간을 줄이는 방법..?

a, b, v = map(int, input().split())
h = (v-b) / (a-b)
print(int(h) if h == int(h) else int(h) + 1)
# 정수인 경우 정수 출력, 아닌 경우 한번 더 올라가야 하므로 +1해서 출력

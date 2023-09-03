n = int(input())
list = list(map(int, input().split()))
v = int(input())
answer = 0

for n in list:
    if n == v:
        answer += 1

print(answer)

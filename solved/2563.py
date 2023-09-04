n = int(input())
page = [[0 for i in range(101)] for i in range(101)]  # 2차원 배열 생성

for i in range(n):
    x, y = map(int, input().split())
    for row in range(x, x + 10):
        for col in range(y, y + 10):
            page[row][col] = 1

answer = 0

for i in page:
    answer += i.count(1)

print(answer)

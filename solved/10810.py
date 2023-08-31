import sys

# 크기가 n인 리스트 생성
n, m = map(int, sys.stdin.readline().split())
basket = [0] * n

# i부터 j까지 바구니의 공을 k로 바꿈
# 인덱스 0이 1번이므로 (i - 1, j)
for l in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for idx in range(i - 1, j):
        basket[idx] = k

for ball in basket:
    print(ball, end=' ')

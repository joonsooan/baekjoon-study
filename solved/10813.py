# 크기가 n인 리스트 생성
n, m = map(int, input().split())
basket = [i+1 for i in range(n)]

# 번호가 i, j인 바구니의 공을 교환
for i in range(m):
    i, j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp
    # basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

for ball in basket:
    print(ball, end=' ')

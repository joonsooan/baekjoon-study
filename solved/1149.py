import sys

n = int(sys.stdin.readline())
dp = [[0, 0, 0]]
for _ in range(n):
    rgb_lst = list(map(int, sys.stdin.readline().split()))
    dp.append(rgb_lst)
# print(dp)

for i in range(2, n+1):
    for j in range(3):  # 빨간색인 경우 전 집의 파란색, 초록색 경우 중 비용이 낮은 걸 선택
        dp[i][j] += min(dp[i-1][(j+1) % 3], dp[i-1][(j+2) % 3])

print(min(dp[n][0], dp[n][1], dp[n][2]))

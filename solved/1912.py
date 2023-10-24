import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
dp = [s[0]]
ans = s[0]

for i in range(1, n):
    new_dp = max(s[i], dp[i-1] + s[i])
    dp.append(new_dp)
    if new_dp > ans:
        ans = new_dp

print(ans)

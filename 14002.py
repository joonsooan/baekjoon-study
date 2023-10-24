n = int(input())
lst = list(map(int, input().split()))
# dp: lst[i]를 마지막 값으로 가지는 가장 긴 증가분수열의 길이
dp = [1]*n
res = set()
res.add(min(lst))  # 가장 긴 증가분수열이면 무조건 가장 작은 값을 포함

for i in range(1, n):
    temp_max_num = -1
    for j in range(i):
        if lst[i] > lst[j]:
            # dp[i] = lst[i]가 추가될 수 있는 증가분수열 중 가장 긴 수열의 길이 + 1
            dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] == dp[j] + 1:  # dp[i]가 업데이트 되었다면
                temp_max_num = lst[i]
    if temp_max_num != -1:
        res.add(temp_max_num)

print(dp)

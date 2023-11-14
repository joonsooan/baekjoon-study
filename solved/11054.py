import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
rev_lst = lst[::-1]
inc = [1 for _ in range(n)]  # 가장 긴 증가하는 부분 수열
dec = [1 for _ in range(n)]  # 가장 긴 감소하는 부분 수열

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if rev_lst[i] > rev_lst[j]:
            dec[i] = max(dec[i], dec[j]+1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = inc[i] + dec[n-i-1] - 1

print(max(result))

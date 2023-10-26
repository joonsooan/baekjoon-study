# 라이브러리 사용
from itertools import permutations

n = int(input())
lst = list(map(int, input().split()))
case_lst = list(permutations(lst, n))  # 모든 경우의 수열 생성
max_ans = 0

for case in case_lst:
    ans = 0
    for i in range(n-1):
        ans += abs(case[i] - case[i+1])
    if ans > max_ans:
        max_ans = ans

print(max_ans)


# 라이브러리 미사용

from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
nlst = []

for three in combinations(lst, 3):  # lst 요소 중 3개씩 고름
    if sum(three) > M:
        continue
    else:
        nlst.append(sum(three))

print(max(nlst))  # m보다 크지 않은 수 중 가장 큰 수 출력

# n, m = map(int, input().split())
# cards = list(map(int, input().split()))
# result = 0

# for i in range(n - 2):
#     for j in range(i + 1, n - 1):
#         for k in range(j + 1, n):
#             total = cards[i] + cards[j] + cards[k]  # 차례로 카드를 모두 더함
#             if total > m:  # 합이 m보다 크면
#                 continue
#             else:
#                 result = max(result, total)

# print(result)

import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())

set_lst = set(lst)  # 중복되는 문자 제거
lst = list(set_lst)  # 다시 리스트로 만듦
lst.sort()  # 먼저 알파벳 순으로 정렬한 후,
lst.sort(key=len)  # 문자열 길이 순으로 정렬
# 최종적으로 길이 1순위, 알파벳 2순위로 정렬됨

for i in lst:
    print(i)

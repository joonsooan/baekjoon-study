import sys

a, b = map(int, sys.stdin.readline().split())
a_lst = list(map(int, sys.stdin.readline().split()))
b_lst = list(map(int, sys.stdin.readline().split()))
a_dict = {key: 1 for key in a_lst}
b_dict = {key: 1 for key in b_lst}

intersection = 0
for x in a_dict:
    if b_dict.get(x) == 1:  # 교집합의 원소인 경우
        intersection += 1

print(len(a_dict) + len(b_dict) - (2 * intersection))

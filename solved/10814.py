import sys

n = int(sys.stdin.readline())
membership_list = []

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    membership_list.append([age, name])

# 가입한 순서대로 리스트에 추가되므로 나이만 정렬하면 끝
membership_list.sort(key=lambda x: x[0])  # age를 기준으로 정렬 (x[0] = age)
for age, name in membership_list:
    print(f"{age} {name}")

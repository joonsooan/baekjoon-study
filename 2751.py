import sys

N = int(sys.stdin.readline())
number_list = []

for i in range(N):
    num = int(sys.stdin.readline())
    number_list.append(num)

number_list.sort(reverse=True)

for num in number_list:
    print(num)
import sys

num_of_cases = int(input())

for i in range(num_of_cases):
    num = int(sys.stdin.readline())
    sum = 0
    for j in range(1, num + 1):
        sum += (num // j) * j
    print(sum)

# 시간복잡도는 N*M인데,
# 어떻게 N으로 만들 수 있을까

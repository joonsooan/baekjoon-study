import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
answer = 0

for time in lst:
    answer += time * n
    n -= 1

print(answer)

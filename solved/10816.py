import sys


n = int(sys.stdin.readline())
my_lst = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target_lst = list(map(int, sys.stdin.readline().split()))

count = {}

for card in my_lst:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in target_lst:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")

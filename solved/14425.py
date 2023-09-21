import sys

n, m = map(int, sys.stdin.readline().split())
my_strings = []
result = 0
for i in range(n):
    my_strings.append(sys.stdin.readline())

for i in range(m):
    test_string = sys.stdin.readline()
    if test_string in my_strings:
        result += 1
print(result)

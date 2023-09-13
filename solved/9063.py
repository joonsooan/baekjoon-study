import sys

n = int(sys.stdin.readline())
x_list = []
y_list = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

min_x = min(x_list)
min_y = min(y_list)
max_x = max(x_list)
max_y = max(y_list)

print((max_x - min_x) * (max_y - min_y))

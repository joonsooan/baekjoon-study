x_list = []
y_list = []
last_x = 0
last_y = 0

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i]) == 1:  # 해당 요소가 한 개만 있는 경우
        last_x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        last_y = y_list[i]

print(last_x, last_y)

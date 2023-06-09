import sys

height_list = []
sum = 0

for i in range(9):
    height = int(sys.stdin.readline())
    height_list.append(height)
    sum += height

height_list.sort()
escape = False

for i in range(9):
    for j in range(i + 1, 9):
        if sum - height_list[i] - height_list[j] == 100:
            spy1 = height_list[i]
            spy2 = height_list[j]
            height_list.remove(spy1)
            height_list.remove(spy2)
            # print(f"list : {height_list}")
            escape = True
            break
    if escape == True:
        break

for i in range(7):
    print(height_list[i])

n = int(input())

max_num = 1
layer = 1

while True:
    if n > max_num:
        max_num += layer * 6
        layer += 1
    else:
        print(layer)
        break

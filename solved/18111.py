import sys
imput = sys.stdin.readline

n, m, b = map(int, input().split())
lst = []

for _ in range(n):
    row = list(map(int, input().split()))
    lst.append(row)
# print(lst)

max_height, min_time = 0, 2 * n * m * 256
height = 0

while True:
    time = 0
    higher_block, lower_block = 0, 0
    # Calculate number of blocks
    for row in lst:
        for block in row:
            if block >= height:
                higher_block += (block - height)
            else:
                lower_block += (height - block)

    if b + higher_block >= lower_block:  # Possible to build height
        time = higher_block * 2 + lower_block
        # print(f"height: {height}, time: {time}")
        if time <= min_time:  # Determine whether it is minimal time
            min_time = time
            max_height = height
    else:  # Impossible to build height -> Stop loop
        break
    height += 1

print(min_time, max_height)

numbers = input().split()

first_num = numbers[0]
second_num = numbers[1]

first_reverse = int(str(first_num)[::-1])
second_reverse = int(str(second_num)[::-1])

if first_reverse > second_reverse:
    print(first_reverse)
else:
    print(second_reverse)
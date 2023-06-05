num_of_data = int(input())

for i in range(num_of_data):
    parenthesis_string = input()
    num_of_left = 0
    num_of_right = 0
    answer = False

    for bracket in parenthesis_string:
        if num_of_left < num_of_right:
            break
        elif bracket == "(":
            num_of_left += 1
        elif bracket == ")":
            num_of_right += 1

    if num_of_left == num_of_right:
        print("YES")
    else:
        print("NO")
x = int(input())

layer = 1  # 층
max_num = 1  # 층의 최대 숫자
prev_max_num = 1  # 이전 층의 최대 숫자
add = 2  # max_num의 증가분
numerator = 0  # 분자
denominator = 0  # 분모
index = 0  # 층에서 숫자의 위치

while True:
    if x > max_num:
        prev_max_num = max_num  # prev_max_num에 현재 max_num 저장
        layer += 1  # 층 이동
        max_num += add
        add += 1
    else:  # x <= max_num
        if x == 1:
            print("1/1")
            break

        elif layer % 2 == 0:  # 짝수 층일 경우 -> 1/n 에서 시작
            numerator = 1  # 분자: 1
            denominator = layer  # 분모: layer
            index = x - prev_max_num - 1  # 층에서 몇 번째 위치에 있는지
            numerator += index
            denominator -= index
            print(f"{numerator}/{denominator}")
            break

        else:  # 홀수 층일 경우 -> n/1 에서 시작
            numerator = layer  # 분자: layer
            denominator = 1  # 분모: 1
            index = x - prev_max_num - 1  # 층에서 몇 번째 위치에 있는지
            numerator -= index
            denominator += index
            print(f"{numerator}/{denominator}")
            break


# n = int(input())
# line = 1

# while n > line:
#     n -= line
#     line += 1

# if line % 2 == 0:
#     up = n
#     down = line - n + 1
# else:
#     up = line - n + 1
#     down = n

# print(f"{up}/{down}")

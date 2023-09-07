# t = int(input())

# for i in range(t):
#     floor_num = 0
#     room_num = 0
#     h, w, n = map(int, input().split())  # w행 h 열의 행렬

#     if n % h == 0:
#         floor_num = h
#     else:
#         floor_num = n % h
#     floor_num = str(floor_num)

#     if h == 1:
#         room_num = n
#     elif n % h == 0:
#         room_num = (n // h)
#     else:
#         room_num = (n // h) + 1

#     if room_num < 10:
#         room_num = str(room_num)
#         room_num = "0" + room_num
#     else:
#         room_num = str(room_num)

#     print(floor_num + room_num)


T = int(input())

for i in range(T):
    floor = 0
    room_num = 0
    h, w, n = map(int, input().split())  # h: 호텔의 층수, n: 몇번째 손님

    floor = n % h
    room_num = (n // h) + 1
    if floor == 0:  # 나머지가 0인 경우 (꼭대기 층일 경우)
        floor = h  # 꼭대기 층의 번호 입력
        room_num -= 1  # 몫이 1 크기 때문에 방번호가 하나 밀림, 따라서 1을 빼줌
        # ex) (20 // 10) + 1 = 3, 실제로 2가 되어야 함

    print(floor * 100 + room_num)

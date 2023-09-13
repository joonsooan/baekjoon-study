import sys

a, b, c = map(int, sys.stdin.readline().split())
max_num = max(a, b, c)  # 가장 큰 숫자

if max_num * 2 < (a + b + c):  # 삼각형을 만족하면 길이를 줄이지 않고 그래도 출력
    print(a + b + c)
else:  # 삼각형을 만족하지 않으면
    new_num = (a + b + c) - max_num - 1  # 가장 긴 변이 최대인 숫자
    print(new_num * 2 + 1)
    # 새로운 가장 긴 변의 길이 + 다른 두 변의 길이
    # new_num + (a + b + c) - max_num = new_num * 2 + 1

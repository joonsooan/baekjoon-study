# 1 << i: 1을 i칸 왼쪽으로 이동 (1 -> 1000)
def get_bit(n, i):  # n의 i번 인덱스의 비트 판정
    return n & (1 << i) != 0


def set_bit(n, i):  # n의 i번 인덱스의 비트를 1로 변경
    return n | (1 << i)


def clear_bit(n, i):  # i번 인덱스의 비트를 0으로 변경
    return n & ~(1 << i)


def clear_left_bit(n, i):  # i번 인덱스를 포함한 왼쪽 비트를 0으로 변경
    return n & (1 << i) - 1


def clear_right_bit(n, i):  # i번 인덱스를 포함한 오른쪽 비트를 0으로 변경
    return n & (-1 << (i+1))


def update_bit(n, i, val):  # i번 인덱스를 val의 값에 따라 변경
    return (n & ~(1 << i)) | ((1 if val else 0) << i)


print(get_bit(9, 3))  # 1 0 0 1
print(get_bit(5, 3))  # 0 1 0 1
print(set_bit(5, 3))  # 0 1 0 1 -> 1 1 0 1
print(clear_bit(9, 3))  # 1 0 0 1 -> 0 0 0 1
print(clear_left_bit(169, 3))  # 10101001 -> 00000001
print(clear_right_bit(169, 3))  # 10101001 -> 10100000
print(update_bit(169, 3, False))

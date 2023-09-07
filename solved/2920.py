def test_scale(list):
    if list[0] == 1:  # 시작이 1인 경우
        for i in range(8):
            if list[i] != ascending[i]:  # 중간에 이상한 값이 있다면
                return "mixed"
        return "ascending"  # 무사히 for문을 돌았을 경우

    elif list[0] == 8:  # 시작이 8인 경우
        for i in range(8):
            if list[i] != descending[i]:
                return "mixed"
        return "descending"

    else:
        return "mixed"


ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

pitch_list = list(map(int, input().split()))
print(test_scale(pitch_list))

def minimum_touch(goal, broken_btn, btn_list):
    if (
        goal >= 98 and goal <= 102
    ) or broken_btn == 9:  # 목표 채널이  98 ~ 102이거나 모든 숫자 버튼이 고장났을 때
        return abs(goal - 100)

    else:
        if broken_btn == 0:  # 고장난 버튼이 없을 때
            return len(str(goal))  # 그냥 목표 채널 그대로 숫자 입력
        else:  # 고장난 버튼이 한 개 이상일 때
            pass  # 함수 넣기


def find_min_diff(goal, btn_list):  # 목표 채널, 고장난 버튼 리스트 입력
    pass

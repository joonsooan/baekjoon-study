import sys


def determine_angle(lst):
    if sum(lst) != 180:
        return "Error"
    lst = set(lst)

    if len(lst) == 1:  # 각이 모두 같은 경우
        return "Equilateral"
    elif len(lst) == 2:  # 두 개의 각이 같은 경우
        return "Isosceles"
    elif len(lst) == 3:  # 각이 모두 다를 경우
        return "Scalene"


lst = []
for i in range(3):
    a = int(sys.stdin.readline())
    lst.append(a)

print(determine_angle(lst))

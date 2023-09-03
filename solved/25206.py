grade_dict = {
    "A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5,
    "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

credit_list = []  # 학점 리스트
grade_list = []  # 등급 리스트
answer = 0
total_score = 0
total_credit = 0

for i in range(20):
    s, c, g = map(str, input().split())
    if g == "P":  # 등급이 P인 과목은 예산에서 제외
        continue
    c = float(c)  # stirng을 실수로 변환
    credit_list.append(c)
    grade_list.append(g)

for i in range(len(credit_list)):
    grade_score = grade_dict[grade_list[i]]  # 딕셔너리에서 등급의 점수 가져옴
    total_score += credit_list[i] * grade_score  # 학점과 과목평점의 곱
    total_credit += credit_list[i]  # 전체 학점

answer = total_score / total_credit
print(answer)

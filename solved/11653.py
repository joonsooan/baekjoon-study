n = int(input())
num = n
divisor_dict = {}  # 약수 딕셔너리
divide = 2  # 나누는 수

while True:
    if n == 1:
        break
    if n % divide == 0:  # 나누어 떨어지면
        if divide not in divisor_dict:  # 딕셔너리에 없는 경우
            divisor_dict[divide] = 1
        else:  # 딕셔너리에 있는 경우
            divisor_dict[divide] += 1
        n /= divide  # 같은 수로 다시 나눌 수 있으므로 나눈 후 저장
    else:  # 나누어 떨어지지 않으면
        divide += 1  # 나누는 수 +1
        if n < divide:  # 더 이상 나눌 수 없으면 중지
            break

# print(divisor_dict)
if num != 1:
    for key, val in divisor_dict.items():
        for i in range(val):  # val의 크기만큼 key를 출력
            print(key)

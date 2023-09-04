ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ary = list(ary)  # 리스트로 변환

n, b = map(int, input().split())
# 변수 초기화
result = ""
quotient = 0
remainder = 0

while True:
    # print(n)
    quotient = n // b
    remainder = n % b
    # print(f"몫: {quotient}, 나머지: {remainder}")
    # print()

    if quotient >= b and remainder >= 10:  # 몫이 b보다 크고 나머지가 10보다 큰 경우
        result += ary[remainder]  # result에 나머지에 해당하는 문자 저장

    elif quotient >= b and remainder < 10:  # 몫이 b보다 크고 나머지가 10보다 작은 경우
        result += str(n % b)  # result에 나머지 저장

    else:  # 몫이 b보다 작은 경우
        result += ary[remainder]
        if quotient != 0:  # 몫이 0인 경우 저장하지 않음
            result += ary[quotient]  # result에 마지막 몫 저장
        break

    n //= b  # n을 몫으로 저장
    # print(result)
    # print()

result = result[::-1]  # 문자열 뒤집기
print(result)

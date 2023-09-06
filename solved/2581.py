m = int(input())
n = int(input())

num_of_divisor = 0  # 약수의 개수
prime_num_list = []  # 소수 리스트

for i in range(m, n + 1):  # m부터 n까지
    for j in range(1, i + 1):
        if i % j == 0:  # 약수가 맞다면
            num_of_divisor += 1
    if num_of_divisor == 2:  # 소수는 약수가 2개
        prime_num_list.append(i)

    num_of_divisor = 0  # 약수의 개수 초기화

# print(prime_num_list)

if len(prime_num_list) == 0:  # 소수가 없는 경우
    print(-1)
else:
    print(sum(prime_num_list))  # 소수의 합
    print(prime_num_list[0])  # 가장 작은 소수

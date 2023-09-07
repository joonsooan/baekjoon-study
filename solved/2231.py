# 1부터 n까지 하나씩 분해합을 생성
# n을 만드는 가장 작은 생성자 구할 수 있음
def find_min_num(n):
    for i in range(n):
        result = i
        num_list = list(map(int, str(i)))
        # print(num_list)
        for num in num_list:  # 모든 수를 다 더한 후 for문 탈출
            result += num
        if result == n:
            return i
        elif i == n-1:  # 모든 경우를 계산했지만 답이 안나옴
            return 0


n = int(input())
print(find_min_num(n))

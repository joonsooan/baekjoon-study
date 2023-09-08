def find_num_of_people(k, n):  # k: 층, n: 호
    floor_ary = [[i for i in range(1, n + 1)]
                 for i in range(k + 1)]  # 2차원 배열 선언
    # print(floor_ary)
    for i in range(1, k + 1):  # i층에 대해 (총 k층까지)
        for j in range(1, n):  # (j + 1)호에 있는 사람의 수 구하기
            floor_ary[i][j] = floor_ary[i-1][j] + floor_ary[i][j-1]
            # 해당 호의 사람의 수는 앞 호의 사람 수 + 밑층 호의 사람 수

    return floor_ary[k][n - 1]  # k층 n호의 사람 수 반환


t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    print(find_num_of_people(k, n))

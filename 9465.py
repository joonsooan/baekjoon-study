import sys
input = sys.stdin.readline

t = int(input())
lst = []
for _ in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(2)]
    lst[0][1] += lst[1][0]  # 첫 번째 열 스티커의 점수는 무조건 포함
    lst[1][1] += lst[0][0]
    # print(lst)
    for j in range(2, n):  # 두 번째 열부터 n-1 번째 열까지 순환
        for i in range(2):  # 두 개의 행에 대해 최댓값 계산
            lst[i][j] += max(lst[0 if i == 1 else 1][j-1],
                             lst[0 if i == 1 else 1][j-2])

    print(max(lst[0][n-1], lst[1][n-1]))  # 마지막 값 2개 중 최댓값 출력

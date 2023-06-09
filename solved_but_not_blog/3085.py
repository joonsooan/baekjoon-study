def check(data):  # 사탕을 바꾸고 난 후 최대 개수를 구하는 함수
    max_count = 1
    for i in range(N):
        count = 1
        for j in range(1, N):
            if data[i][j] == data[i][j - 1]:  # 고른 사탕 2개의 색깔이 같을 때
                count += 1  # 연속되는 경우 1을 더함
            else:
                count = 1  # 연속되지 않을 때 1로 초기화
            max_count = max(max_count, count)  # for문을 한번 돌 때마다 max_count를 업데이트

        count = 1
        for j in range(1, N):
            if data[j][i] == data[j - 1][i]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    return max_count  # 2개의 for문을 돌면서 max_count가 가장 큰 값이 나오게 됨


N = int(input())
data = [list(input()) for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(N):
        if j + 1 < N:  # 가장 오른쪽 줄은 실행하지 않음
            data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j]
            count = check(data)  # 바꾼 이후 최대 개수를 구함
            answer = max(answer, count)
            data[i][j], data[i][j + 1] = data[i][j + 1], data[i][j]  # 원상복귀

        if i + 1 < N:  # 가장 밑 줄은 실행하지 않음
            data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]
            count = check(data)
            answer = max(answer, count)
            data[i][j], data[i + 1][j] = data[i + 1][j], data[i][j]

print(answer)  # answer을 계속 최대값으로 업데이트 하고 마지막에 출력함

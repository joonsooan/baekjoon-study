import sys
input = sys.stdin.readline

n, m = map(int, input().split())
test_lst = []
for _ in range(m):
    test_lst.append(list(map(str, input().split())))

candidate_lst = [[-1, -1] for _ in range(n)]
for i in range(m):
    idx = int(test_lst[i][0]) - 1
    feature = test_lst[i][1]
    feature_exist = int(test_lst[i][2])

    if feature == 'P':
        candidate_lst[idx][0] = feature_exist
    else:
        candidate_lst[idx][1] = feature_exist
# print(candidate_lst)

min_plant, max_plant = 0, 0
for i in range(n):
    # 실험을 하지 않은 경우는 가능성 있음
    if candidate_lst[i][0] == -1 and candidate_lst[i][1] == -1:
        max_plant += 1
    else:
        # 무조건 식물인 경우
        if candidate_lst[i][0] == 1 and candidate_lst[i][1] == 0:
            min_plant += 1
            max_plant += 1
        # 가능성이 있는 경우
        elif candidate_lst[i][0] == -1 and candidate_lst[i][1] == 0:
            max_plant += 1
        elif candidate_lst[i][0] == 1 and candidate_lst[i][1] == -1:
            max_plant += 1


print(min_plant, max_plant)

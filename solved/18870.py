import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

sorted_lst = sorted(list(set(lst)))  # 중복 제거, 오름차순 정렬
sorted_dic = {val: key for key, val in enumerate(
    sorted_lst)}  # sorted_lst의 요소와 인덱스를 각각 key, val로 반환하여 딕셔너리 생성

for num in lst:  # 딕셔너리에 접근하여 key에 따른 val 출력
    print(sorted_dic[num], end=' ')

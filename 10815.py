def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 원하는 값 찾은 경우
        if array[mid] == target:
            return 1
        # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
        elif array[mid] > target:
            end = mid - 1
        # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
        else:
            start = mid + 1

    return 0


n = int(input())
my_lst = list(map(int, input().split()))
sorted_lst = sorted(my_lst)

m = int(input())
card_lst = list(map(int, input().split()))

for i in range(m):
    target = card_lst[i]
    length = len(sorted_lst)
    result = binary_search(sorted_lst, target, 0, length - 1)
    print(result, end=' ')

import sys


def generate_numbers(lst, length, current=[]):
    res_lst = []
    if length == 0:
        res = int(''.join(map(str, current)))
        res_lst.append(res)

    for num in lst:
        current.append(num)
        generate_numbers(lst, length - 1, current)
        current.pop()

    return res_lst


# 변수, 리스트 입력
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
btn_lst = [i for i in range(10)]
broken_btn_lst = list(map(int, sys.stdin.readline().split()))
for broken_btn in broken_btn_lst:
    btn_lst.remove(broken_btn)
# print(btn_lst)

# 한 자리부터 len(n)자리 수까지 만들 수 있는 모든 숫자 생성
for i in range(1, len(str(n))+1):
    print(generate_numbers(btn_lst, i))

# n과 생성한 숫자 비교

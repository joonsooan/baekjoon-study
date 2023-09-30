import sys

n = int(sys.stdin.readline())
standing = list(map(int, sys.stdin.readline().split()))
stack = []
target = 1

while standing:
    if standing[0] == target:
        standing.pop(0)
        target += 1
    else:
        stack.append(standing.pop(0))

    # stack의 가장 끝 요소가 target인지 확인
    # 여러 개가 가능할 수 있으므로 while문 사용
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break

if not stack:  # stack 안에 아무것도 없다면
    print('Nice')
else:
    print('Sad')

# 굳이 temp_stk를 만들지 않고 마지막에 stack의 길이로 판단

# n = int(sys.stdin.readline())
# lst = list(map(int, sys.stdin.readline().split()))
# stack = []
# temp_stk = []
# now = 1
# sad = False

# for num in lst:
#     # temp_stk의 가장 끝 요소가 stack에 들어갈 수 있는지 확인
#     while True:  # 여러 개가 들어갈 수 있으므로 while문 사용
#         if len(temp_stk) != 0 and temp_stk[-1] == now:
#             stack.append(now)
#             temp_stk.pop()
#             now += 1
#         else:
#             break

#     if num == now:
#         stack.append(num)
#         now += 1
#     elif len(temp_stk) == 0:
#         temp_stk.append(num)
#     else:  # temp_stk에 요소가 있는 경우
#         if temp_stk[-1] < num:  # 마지막 요소보다 새 요소가 큰 경우
#             sad = True
#             break
#         else:  # 새 요소가 더 작은 경우
#             temp_stk.append(num)

# if sad:
#     print("Sad")
# else:
#     print("Nice")

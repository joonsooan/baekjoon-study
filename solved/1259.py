# while True:
#     palindrome = True
#     n = input()
#     if n == "0":  # 0인 경우 종료
#         break
#     for i in range(len(n)):
#         if n[i] != n[len(n) - i - 1]:  # 대칭인 수가 다를 경우
#             palindrome = False
#             print("no")  # no 출력 후 for문 탈출
#             break
#     if palindrome == True:  # for문을 끝까지 돌았다면 (if문에 들어간 적 없음)
#         print("yes")

while True:
    n = input()
    if n == '0':
        break
    elif n == n[::-1]:  # 문자열이 뒤집은 문자열과 일치하면
        print('yes')
    else:
        print('no')

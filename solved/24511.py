import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))  # 초기 순열
m = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))

que_lst = []
for i in range(n):
    if a[i] == 0:  # 자료구조가 큐인 경우
        que_lst.append(b[i])
que_lst.reverse()

if not que_lst:  # 모든 요소가 스택인 경우
    print(' '.join(map(str, c)))

else:  # 큐가 적어도 하나 있는 경우
    if len(que_lst) >= m:
        for i in range(m):
            print(que_lst[i], end=' ')
    else:  # que_lst 길이가 m보다 작은 경우
        print(' '.join(map(str, que_lst)), end=' ')
        for i in range(m - len(que_lst)):
            print(c[i], end=' ')

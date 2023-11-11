import sys
from collections import deque
input = sys.stdin.readline


def find_order():
    n, m = map(int, input().split())
    deq = deque(list(map(int, sys.stdin.readline().split())))
    cnt = 0

    while deq:
        max_prior = max(deq)
        front = deq.popleft()
        m -= 1
        if max_prior == front:
            cnt += 1
            if m < 0:  # front가 m이 가리키는 변수인 경우
                print(cnt)
                break
        else:
            deq.append(front)
            if m < 0:  # front가 m이 가리키는 변수인 경우 -> 인덱스 m을 맨 뒤로 초기화
                m = len(deq) - 1


t = int(input())
for _ in range(t):
    find_order()

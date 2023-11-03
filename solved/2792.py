import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [int(input()) for _ in range(m)]
start, end = 1, max(lst)
min_jealous = max(lst)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    # Calculating number of students
    for jewel in lst:
        cnt += (jewel // mid)
        if jewel % mid > 0:
            cnt += 1

    # Too small mid value
    if cnt > n:
        start = mid + 1
    # Too big mid value / We can find smaller mid
    else:  # cnt <= n
        if mid < min_jealous:
            min_jealous = mid
        end = mid - 1

print(min_jealous)

# 처음엔 색깔별로 학생 수를 나눠줘야 한다고 생각했지만,
# 그게 아니라 질투의 최대값을 이분탐색으로 구하는 방법이었다.
# 질투의 최댓값을 정해주면 각 색깔별로 학생이 몇 명 배정받는지가 자동으로 결정
# 배정받은 학생 수가 n보다 많으면 질투의 최댓값 증가,
# 학생 수가 n보다 작으면 질투의 최댓값 감소,
# 학생 수가 n과 같아도 질투의 최댓값 감소(더 작은 값을 찾을 수 있음)

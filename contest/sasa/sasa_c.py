import sys
input = sys.stdin.readline

hand, machine_hand = '2'*100, '2'*100

for _ in range(101):
    k = int(input())

    # 모르는 경우
    if k != 100:
        # 다음에 낼 손 모양 정하기
        print(f"? {hand}")
        sys.stdout.flush()

    # 정답인 경우
    else:
        print(f"! {machine_hand}")
        sys.stdout.flush()
        break

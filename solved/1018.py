import sys


def calculate_repaint(lst, row, col):  # 칠하는 횟수를 계산하는 함수
    repaint = 0
    repaint_W = 0
    repaint_B = 0
    # "W" : True, "F" : False

    # 처음 칸을 W로 설정했을 때
    right_color = True
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if lst[i][j] == right_color:   # 색깔이 맞으면 패스
                pass
            else:                          # 색깔이 틀리면 색칠
                repaint_W += 1
            right_color = not right_color  # 다음 칸을 검색할 때는 색깔 반전해서 확인
        right_color = not right_color      # 다음 줄로 넘어갈 때는 색깔이 그대로

    # 처음 칸을 B로 설정했을 때
    right_color = False
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if lst[i][j] == right_color:
                pass
            else:
                repaint_B += 1
            right_color = not right_color
        right_color = not right_color

    repaint = min(repaint_B, repaint_W)  # 둘 중 더 작은 경우가 정답
    return repaint


n, m = map(int, sys.stdin.readline().split())
board = [[] for _ in range(n)]

for i in range(n):
    line = sys.stdin.readline().strip()
    board[i] = list(line)

converted_board = [[True if cell == 'W' else False for cell in row]
                   for row in board]
# 하얀색을 True, 검은색을 False로 변환

result = 64  # 8 x 8 체스판의 최대 칠해야 하는 횟수

# 8 X 8의 범위만큼 한번씩 접근하는 코드
for row in range(n - 7):
    for col in range(m - 7):
        repaint = calculate_repaint(converted_board, row, col)
        result = min(result, repaint)  # 한 판을 계산할 때마다 최소 횟수 업데이트

print(result)

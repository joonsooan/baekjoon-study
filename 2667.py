# bfs
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
result = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, x, y):

    q = deque()
    q.append([x, y])
    graph[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:  # 아직 방문하지 않았으면 cnt += 1
                    graph[nx][ny] = 0
                    q.append([nx, ny])
                    cnt += 1

    return cnt


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:  # 아직 방문하지 않았으면 bfs
            cnt = bfs(graph, i, j)  # cnt: 단지 내 아파트 수
            result.append(cnt)

result.sort()
print((len(result)))
for i in result:
    print(i)

# dfs

# input = sys.stdin.readline

# n = int(input())

# graph = []
# result = []
# cnt = 0

# for _ in range(n):
#     graph.append(list(map(int, input().rstrip())))

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]


# def dfs(x, y):
#     global cnt

#     if 0 <= x < n and 0 <= y < n:
#         if graph[x][y] == 1:
#             cnt += 1
#             graph[x][y] = 0

#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 dfs(nx, ny)


# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             dfs(i, j)
#             result.append(cnt)
#             cnt = 0

# result.sort()
# print(len(result))
# for i in result:
#     print(i)

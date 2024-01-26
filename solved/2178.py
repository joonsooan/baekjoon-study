# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# lst = []
# for _ in range(n):
#     lst.append(list(input().rstrip()))

# visited = [[False] * m for _ in range(n)]
# depth = [[n*m] * m for _ in range(n)]
# depth[0][0] = 1


# def bfs(v):
#     q = deque([v])
#     x, y = v[0], v[1]
#     visited[x][y] = True

#     while q:
#         v = q.popleft()
#         x, y = v[0], v[1]
#         visited[x][y] = True

#         if x >= 1:
#             if not visited[x-1][y] and lst[x-1][y] == '1':
#                 q.append([x-1, y])
#                 visited[x-1][y] = True
#                 depth[x-1][y] = min(depth[x-1][y], depth[x][y]+1)

#         if y >= 1:
#             if not visited[x][y-1] and lst[x][y-1] == '1':
#                 q.append([x, y-1])
#                 visited[x][y-1] = True
#                 depth[x][y-1] = min(depth[x][y-1], depth[x][y]+1)

#         if x < n-1:
#             if not visited[x+1][y] and lst[x+1][y] == '1':
#                 q.append([x+1, y])
#                 visited[x+1][y] = True
#                 depth[x+1][y] = min(depth[x+1][y], depth[x][y]+1)

#         if y < m-1:
#             if not visited[x][y+1] and lst[x][y+1] == '1':
#                 q.append([x, y+1])
#                 visited[x][y+1] = True
#                 depth[x][y+1] = min(depth[x][y+1], depth[x][y]+1)


# bfs([0, 0])
# print(depth[-1][-1])


import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] == 1:
                q.append([next_x, next_y])
                graph[next_x][next_y] = graph[x][y] + 1

    return graph[n-1][m-1]


print(bfs(0, 0))

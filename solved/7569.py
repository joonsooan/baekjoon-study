from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque([])
answer = 0

m, n, h = map(int, input().split())
graph = [[list(map(int, sys.stdin.readline().split()))
          for _ in range(n)] for _ in range(h)]


def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if graph[nx][ny][nz] == 0:
                    q.append([nx, ny, nz])
                    graph[nx][ny][nz] = graph[x][y][z] + 1


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append([i, j, k])

bfs()

for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))

print(answer - 1)

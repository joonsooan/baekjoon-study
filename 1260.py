from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n+1)] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)


# dfs
def dfs(v):
    visited1[v] = True
    print(v, end=" ")

    for i in range(1, n+1):
        if not visited1[i] and graph[v][i] == 1:  # 방문하지 않고 연결되어있을 때
            dfs(i)


# bfs
def bfs(v):
    q = deque([v])
    visited2[v] = True

    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n+1):
            if not visited2[v] and graph[v][i] == 1:
                q.append(i)
                visited2[i] = True


dfs(v)
print()
bfs(v)
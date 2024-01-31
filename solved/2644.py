from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
links = [1] * (n+1)
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# BFS
def bfs(graph, v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        v = q.popleft()
        if v == b:
            return links[v]

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                links[i] += links[v]

    return 0


# print(bfs(graph, a) - 1)


# DFS
global result
result = 0


def dfs(v, num):
    global result
    num += 1
    visited[v] = True

    if v == b:
        result = num

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)


dfs(a, 0)
print(result-1)

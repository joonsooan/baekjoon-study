import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    f, t = map(int, input().split())

    if graph[f] == []:
        graph[f] = [t]
    else:
        graph[f].append(t)

    if graph[t] == []:
        graph[t] = [f]
    else:
        graph[t].append(f)


def bfs(graph, v, visited):
    ans = -1  # 1은 무조건 방문하므로 최소 0
    q = deque()
    q.append(v)

    while q:
        vertex = q.popleft()

        if not visited[vertex]:
            visited[vertex] = True
            ans += 1

            for i in graph[vertex]:
                q.append(i)

    return ans


print(bfs(graph, 1, visited))

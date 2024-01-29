from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
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

# print(graph)


def bfs(graph, a, b):  # a: Start vertex, b: End vertex
    cnt = 0
    q = deque([a])
    visited[a] = True

    while q:
        v = q.popleft()
        print(v, end=" ")

        for i in range(1, n+1):
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1

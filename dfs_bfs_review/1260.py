from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]  # 정점의 연결 관계를 확인하기 위한 그래프

for _ in range(m):
    x, y = map(int, input().split())  # 연결된 정점들은 1로 표시
    graph[x][y] = 1
    graph[y][x] = 1

visited1 = [False] * (n+1)  # dfs 방문 체크용
visited2 = [False] * (n+1)  # bfs 방문 체크용


# dfs
def dfs(v):
    visited1[v] = True  # 방문했으니 체크표시
    print(v, end=" ")  # 방문한 정점 출력

    for i in range(1, n+1):  # 1번 정점부터 n번 정점까지 체크
        if not visited1[i] and graph[v][i] == 1:  # 방문하지 않고 연결된 정점
            dfs(i)  # 재귀로 반복


# bfs
def bfs(v):
    q = deque([v])
    visited2[v] = True

    while q:  # 덱에 정점이 없어질 때까지 수행
        v = q.popleft()
        print(v, end=" ")

        for i in range(1, n+1):  # 1번 정점부터 n번 정점까지 체크
            if not visited2[i] and graph[v][i] == 1:  # 방문하지 않고 연결된 정점
                q.append(i)  # 덱에 추가
                visited2[i] = True  # 방문 표시


dfs(v)
print()
bfs(v)

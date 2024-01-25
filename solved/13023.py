import sys
input = sys.stdin.readline

n, m = map(int, input().split())
relations = [[] for _ in range(n)]  # Max relation num = 2000
visited = [False] * 2001
ans = False

# 연결 리스트로 연결 관계 저장
for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)


def dfs(idx, depth):  # depth = 연결된 관계의 수, 4개면 5명이 연결됨
    global ans
    visited[idx] = True

    if depth == 4:  # 연결된 관계의 수가 4인 경우, 5명이 연결되어있음 -> 1 출력
        ans = True
        return

    for i in relations[idx]:
        if not visited[i]:  # 연결되어있지만 아직 방문하지 않은 정점
            visited[i] = True
            dfs(i, depth + 1)  # 이 정점에서 dfs 수행
            visited[i] = False  # dfs 수행 후 이전 정점으로 이동


for i in range(n):
    dfs(i, 0)  # i부터 시작해 연결된 친구 관계 탐색
    visited[i] = False
    if ans:
        break

if ans:
    print(1)
else:
    print(0)

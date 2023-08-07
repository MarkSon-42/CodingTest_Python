from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

# 연결된 정점을 입력
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1


# dfs와 bfs 그래프의 방문 여부를 담을 리스트
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)


def dfs(v):
    # 방문 처리
    visited_dfs[v] = True
    # 방문 후, 정점 출력
    print(v, end=" ")
    # 방문 기록이 없고, 인덱스에 값이 있다면(연결되어 있다면)
    for i in range(1, N + 1):
        if not visited_dfs[i] and graph[v][i] == 1:
            #  방문 (재귀)
            dfs(i)


def bfs(v):




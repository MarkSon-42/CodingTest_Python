from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)] # 방문하지 않음으로 초기화 0 : (False)

# 연결된 정점을 입력
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1



# dfs와 bfs 그래프의 방문 여부를 담을 리스트
visited_dfs = [0] * (N + 1)
visited_bfs = visited_dfs.copy()


def dfs(V):
    visited_dfs[V] = 1  # 방문 처리 : 1 (True)
    print(V, end=' ')
    for i in range(1, N + 1):
        if graph[V][i] == 1 and visited_dfs[i] == 0:
            dfs(i)


def bfs(V):
    queue = [V]
    visited_bfs[V] = 1
    while queue:
        V = queue.pop(0)  # 방문 노드 제거
        print(V, end=' ')
        for i in range(1, N + 1):
            if graph[V][i] == 1 and visited_bfs[i] == 0:
                queue.append(i)
                visited_bfs[i] = 1


dfs(V)
print()
bfs(V)
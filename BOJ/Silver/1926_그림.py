from collections import deque


def bfs(x, y):
    pass


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
answer = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            cnt += 1
            answer = max(bfs(i, j), answer)

print(cnt)
print(answer)

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

for _ in range(int(input())):
    n = int(input())
    wall = [input().split() for _ in range(n)]

    q = deque()
    q.append((n - 1, 0))
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[n - 1][0] = 1
    while len(q):
        r, c = q.popleft()
        v = visited[r][c] + 1

        # Rule 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < n and 0 <= nc < n) or visited[nr][nc]:
                continue
            if wall[nr][nc] == "H":
                q.append((nr, nc))
                visited[nr][nc] = v

        # Rule 2
        if r > 0:
            for i in range(1, 4, 2):
                nc = c + dc[i]
                for _ in range(2):
                    nc += dc[i]
                    if not (0 <= nc < n):
                        break

                    if not (
                        wall[r - 1][c] == "."
                        and wall[r - 1][nc - dc[i]] == "."
                        and wall[r - 1][nc] == "."
                        and wall[r][nc - dc[i]] == "."
                    ):
                        break

                    if wall[r][nc] == "H" and not visited[r][nc]:
                        q.append((r, nc))
                        visited[r][nc] = v
                        break

        # Rule 3
        if r > 1:
            if (
                wall[r - 1][c] == "."
                and wall[r - 2][c] == "H"
                and not visited[r - 2][c]
            ):
                q.append((r - 2, c))
                visited[r - 2][c] = v

        # Rule 4
        if r > 0 and c > 0:
            if (
                wall[r - 1][c - 1] == "H"
                and wall[r - 1][c] == "."
                and wall[r][c - 1] == "."
                and not visited[r - 1][c - 1]
            ):
                q.append((r - 1, c - 1))
                visited[r - 1][c - 1] = v

        # Rule 5
        if r > 0 and c + 1 < n:
            if (
                wall[r - 1][c + 1] == "H"
                and wall[r - 1][c] == "."
                and wall[r][c + 1] == "."
                and not visited[r - 1][c + 1]
            ):
                q.append((r - 1, c + 1))
                visited[r - 1][c + 1] = v

    for r in range(n):
        for c in range(n):
            if wall[r][c] == "H" and not visited[r][c]:
                print(-1, end=" ")
            else:
                print(visited[r][c], end=" ")
        print()

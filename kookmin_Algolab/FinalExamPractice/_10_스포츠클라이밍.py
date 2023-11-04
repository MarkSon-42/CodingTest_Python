from collections import deque

def optimize_code():
    n = int(input())
    wall = [list(input()) for _ in range(n)]

    q = deque()
    q.append((n - 1, 0))
    wall[n - 1][0] = 1

    while q:
        r, c = q.popleft()
        v = wall[r][c] + 1

        # Rule 1: 인접한 상하좌우로 이동하는 경우
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < n) or wall[nr][nc] != ".":
                continue
            q.append((nr, nc))
            wall[nr][nc] = v

        # Rule 2: 1칸 또는 2칸 위로 이동하는 경우
        if r > 0:
            if c > 0 and wall[r - 1][c - 1] == "." and wall[r][c - 1] == "." and wall[r - 1][c] == ".":
                if wall[r - 2][c - 1] == "H":
                    q.append((r - 2, c - 1))
                    wall[r - 2][c - 1] = v
                if wall[r - 1][c - 2] == "H":
                    q.append((r - 1, c - 2))
                    wall[r - 1][c - 2] = v

            if wall[r - 1][c] == ".":
                if wall[r - 2][c] == "H":
                    q.append((r - 2, c))
                    wall[r - 2][c] = v
                if wall[r - 1][c - 1] == "H":
                    q.append((r - 1, c - 1))
                    wall[r - 1][c - 1] = v

        # Rule 3: 왼쪽 대각선 위로 이동하는 경우
        if r > 0 and c < n - 1 and wall[r - 1][c + 1] == "." and wall[r][c + 1] == "." and wall[r - 1][c] == ".":
            if wall[r - 2][c + 1] == "H":
                q.append((r - 2, c + 1))
                wall[r - 2][c + 1] = v
            if wall[r - 1][c + 2] == "H":
                q.append((r - 1, c + 2))
                wall[r - 1][c + 2] = v

    # 결과 출력
    for row in wall:
        for cell in row:
            if cell == "H":
                print(-1, end=" ")
            else:
                print(cell, end=" ")
        print()

optimize_code()

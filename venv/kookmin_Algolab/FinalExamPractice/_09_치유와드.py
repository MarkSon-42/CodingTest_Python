T = int(input())

for _ in range(T):
    n, m = map(int, input().strip().split())
    a, b = map(int, input().strip().split())

    dead = [list(map(int, input().split())) for i in range(a)]
    ward = [list(map(int, input().split())) for i in range(b)]
    maps = [[0] * n for _ in range(n)]

    # 거리와 점수 계산을 위한 미리 계산
    for p in dead:
        r, c = p
        for i in range(n):
            for j in range(n):
                p_dist = max(abs(r - i), abs(c - j))
                maps[i][j] -= max(m - p_dist + 1, 0)

    for h in ward:
        r, c = h
        for i in range(n):
            for j in range(n):
                h_dist = abs(r - i) + abs(c - j)
                maps[i][j] += max(m - h_dist + 1, 0)

    # maps 값 한 번에 갱신
    for p in dead:
        maps[p[0]][p[1]] += 1

    for h in ward:
        maps[h[0]][h[1]] -= 1

    for i in maps:
        print(*i)

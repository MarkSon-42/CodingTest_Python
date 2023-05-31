t = int(input())
for _ in range(t):
    n, m = map(int, input().strip().split())
    a, b = map(int, input().strip().split())

    poison_list = []
    heal_list = []
    for _ in range(a):
        poison_list.append(list(map(int, input().strip().split())))
    for _ in range(b):
        heal_list.append(list(map(int, input().strip().split())))

    safe_list = [[0] * n for i in range(n)]

    for p in poison_list:
        safe_list[p[0]][p[1]] += 1
    for h in heal_list:
        safe_list[h[0]][h[1]] -= 1

    for i in range(n):
        for j in range(n):
            for p in poison_list:
                p1 = p[0]
                p2 = p[1]
                pa = max(abs(p1 - i), abs(p2 - j))
                safe_list[i][j] -= max(m - pa + 1, 0)
            for h in heal_list:
                h1 = h[0]
                h2 = h[1]
                ha = abs(h1 - i) + abs(h2 - j)
                safe_list[i][j] += max(m - ha + 1, 0)

    for i in safe_list:
        print(" ".join(map(str, i)))

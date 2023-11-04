n, m = tuple(map(int, input().split()))

coin_map = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]
for _ in range(m):
    r, c = map(int, input().split())
    coin_map[r][c] = r * c

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(coin_map[i][j], end=' ')
    print()
n, m = tuple(map(int, input().split()))
cnt = 1
coin_map = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]
for _ in range(m):
    r, c = map(int, input().split())
    coin_map[r][c] = cnt
    cnt += 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(coin_map[i][j], end=' ')
    print()
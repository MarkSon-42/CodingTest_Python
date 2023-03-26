n, k= map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input))
coins.sort(reverse=True)


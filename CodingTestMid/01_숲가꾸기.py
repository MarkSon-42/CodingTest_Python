from collections import deque

t = int(input())
for _ in range(t):
    m, c, k, p = map(int, input().split(' '))  # m격자크기,c나무의수,k지력회복크기,p시뮬레이션반복횟수

    energy = [list(map(int, input().split(' '))) for _ in range(m)]
    trees = deque()
    dead = list()
    for _ in range(c):
        x, y, z = map(int, input().split(' '))
        trees.append([z, x, y])

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    def absorb():
        len_ = len(trees)
        for _ in range(len_):
            z, x, y = trees.popleft()
            if energy[x][y] < z:
                dead.append([z, x, y])
            else:
                energy[x][y] -= z
                trees.append([z + 1, x, y])

        while dead:
            z, x, y = dead.pop()
            energy[x][y] += z // 2

    def breed():
        for z, x, y in list(trees):
            if z % 5 == 0:
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]

                    if nx < 0 or nx >= m or ny < 0 or ny >= m:
                        continue

                    trees.appendleft([1, nx, ny])

        for i in range(m):
            for j in range(m):
                energy[i][j] += k

    for i in range(p):
        absorb()
        breed()

    print(len(trees))

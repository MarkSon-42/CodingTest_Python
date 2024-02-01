import sys

sys.setrecursionlimit(10 * 6)


def dfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
# https://coarmok.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%ACpython-%EB%B0%B1%EC%A4%80-2146%EB%B2%88-%EB%8B%A4%EB%A6%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0

import sys
from collections import deque

sys.setrecursionlimit(10**6)

# dfs로 섬 라벨링 하기
# 문제에서 섬은 모두 1로 입력이 주어지기 때문에
# 같은 섬끼리 라벨링을 하기 위해서
# count를 2부터 시작해서 dfs를 돌 때 마다 count++

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

answer = sys.maxsize


def dfs(i, j):
    global cnt
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if arr[i][j] == 1:
        arr[i][j] = cnt
        for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
            nx = dx + i
            ny = dy + j
            dfs(nx, ny)
        return True


# 예시
# 222----333
# 2222----33
# --22----22
# --222----3
# ---------3
# ----------
# ------44--
# ------444-

# 이제 각 섬에서 다른섬 까지 거리 중 최솟값 구하기
# 거리의 최솟값은 최단거리
# 최단거리는 bfs!


def bfs(num):
    pass


cnt = 2
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            cnt += 1
for i in range(2, cnt):
    bfs(i)

print(answer)

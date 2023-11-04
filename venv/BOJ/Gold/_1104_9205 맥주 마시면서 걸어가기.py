# 1000 - x abs   1000 - y abs 아니면 무조건 sad 처리부터

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    conv = [[list(input().split())] for _ in range(n)]
    fstv_x, fstv_y = map(int, input().split())


# 내가 뭘 모르는 걸까...?

# -> bfs
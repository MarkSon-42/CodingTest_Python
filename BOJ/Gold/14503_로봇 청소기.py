N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
room[r][c] = 2  # 청소 되었음을 2로 나타내기
count = 1

while True:
    check = False
    for _ in range(4):
        d = (d + 3) % 4

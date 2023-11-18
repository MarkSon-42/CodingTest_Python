# https://unie2.tistory.com/1126

t = int(input())


def check():
    # 오른쪽, 아래, 오른쪽아래 대각선, 왼쪽아래 대각선
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == "o":
                for direction in range(4):
                    nx = i
                    ny = j
                    cnt = 0

                    while 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == "o":
                        cnt += 1
                        nx += dx[direction]
                        ny += dy[direction]
                    if cnt >= 5:
                        return "YES"
    return "NO"


for tc in range(1, t + 1):
    n = int(input())
    grid = [input() for _ in range(n)]

    print(f"{tc} {check()}")

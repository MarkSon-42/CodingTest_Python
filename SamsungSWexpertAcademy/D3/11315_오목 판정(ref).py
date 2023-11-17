t = int(input())


def check():
    for i in range(n):
        for j in range(n):
            if data[i][j] == "o":
                for dir in range(4):
                    nx = i
                    ny = j
                    cnt = 0

                    while 0 <= nx < n and 0 <= ny < n and data[nx][ny] == "o":
                        cnt += 1
                        nx += dx[dir]
                        ny += dy[dir]
                    if cnt >= 5:
                        return "YES"
    return "NO"


for tc in range(1, t + 1):
    n = int(input())
    data = [input() for _ in range(n)]

    print("#%d %s" % (tc, check()))

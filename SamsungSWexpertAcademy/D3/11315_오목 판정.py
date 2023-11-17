tc = int(input())

for t in range(1, tc + 1):
    n = int(input())
    grid = [[list(map(str, input().split()))] for _ in range(n)]
    answer = "NO"
    for i in range(n):
        if answer == "YES":
            break
        for j in range(n):
            if grid[i][j : j + 5] == "ooooo":
                answer = "YES"
                break
    for i in range(n):
        if answer == "YES":
            break
        for j in range(n):
            if grid[i : i + 5][j] == "ooooo":
                answer = "YES"
                break

#  이런 병슨같은 빡구현은 하지마쇼..
#

def solution(n):
    spiral = [[0 for _ in range(n)] for _ in range(n)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direction_index = 0

    x, y = 0, 0

    for num in range(1, n ** 2 + 1):
        spiral[x][y] = num
        next_x, next_y = x + directions[direction_index][0], y + directions[direction_index][1]

        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or spiral[next_x][next_y] != 0:
            direction_index = (direction_index + 1) % 4
            x, y = x + directions[direction_index][0], y + directions[direction_index][1]
        else:
            x, y = next_x, next_y

    return spiral


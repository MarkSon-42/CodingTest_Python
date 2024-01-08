from queue import Queue

q = Queue()
answer = [[0] * 5 for _ in range(5)]
order = 1
grid = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1],
]
visited = [[False] * 5 for _ in range(5)]


def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] == 1


def push(x, y):
    global order
    answer[x][y] = order
    order += 1
    visited[x][y] = True
    q.put((x, y))


def bfs():
    dx = [1, 0]
    dy = [0, 1]

    while not q.empty():
        curr_pos = q.get()
        x, y = curr_pos

        for i in range(2):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if can_go(new_x, new_y):
                push(new_x, new_y)


# Sample usage
push(0, 0)
bfs()

# Print the result
for row in answer:
    print(row)

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

# 가능한 모든 모양을 전부 적어줌 (완탐 테크닉중 하나)

shapes = [
    [[1, 1, 0],
     [1, 0, 0],
     [0, 0, 0]],

    [[1, 1, 0],
     [0, 1, 0],
     [0, 0, 0]],

    [[0, 1, 0],
     [1, 1, 0],
     [0, 0, 0]],

    [[1, 0, 0],
     [1, 1, 0],
     [0, 0, 0]],

    [[1, 1, 1],
     [0, 0, 0],
     [0, 0, 0]],

    [[1, 0, 0],
     [1, 0, 0],
     [1, 0, 0]],

]

def get_max_sum(x, y):
    max_sum = 0
    for i in range(6):  # 6가지 모양을 검사
        is_possible = True
        sum_ = 0
        for dx in range(0, 3):
            for dy in range(0, 3):
                if shapes[i][dx][dy] == 0:
                    continue  # 근데 0 이거는 뭐 필요없지 않나?
                if x + dx >= n or y + dy >= m:
                    is_possible = False
                else:
                    sum_ += grid[x + dx][y + dy]

        if is_possible:
            max_sum = max(max_sum, sum_)
    return max_sum

answer = 0

for i in range(n):
    for j in range(m):
        answer = max(answer, get_max_sum(i, j))

print(answer)


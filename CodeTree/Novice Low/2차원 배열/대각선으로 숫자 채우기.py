n, m = tuple(map(int, input().split()))
num = 1
answer = [[0 for _ in range(m)] for _ in range(n)]

for start_col in range(m):
    curr_row = 0
    curr_col = start_col

    while 0 <= curr_col and curr_row < n:
        answer[curr_row][curr_col] = num

        curr_row += 1
        curr_col -= 1
        num += 1

for start_row in range(1, n):
    curr_row = start_row
    curr_col = m - 1

    while 0 <= curr_col and curr_row < n:
        answer[curr_row][curr_col] = num

        # 변수 업데이트
        curr_row += 1
        curr_col -= 1
        num += 1

for row in range(n):
    for col in range(m):
        print(answer[row][col], end=' ')
    print()


# 너... 무 어렵다.
# 코드 전부 손으로 쓰는게 답

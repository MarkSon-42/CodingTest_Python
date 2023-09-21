rows = 3
cols = 3
start = 1

matrix_1st = []
matrix_2st = []
matrix_answer = []

for row in range(rows):
    row_list = []
    for col in range(cols):
        row_list.append(start)
        start += 1
    matrix_1st.append(row_list)

start = 2

for row in range(rows):
    row_list_ = []
    for col in range(cols):
        row_list_.append(start)
        start += 1
    matrix_2st.append(row_list_)

for row in range(rows):
    for col in range(cols):
        matrix_answer.append(matrix_1st[row][col] * matrix_2st[row][col])

cnt = 0
for c in matrix_answer:
    if cnt == 3:
        print()
        cnt = 0
    cnt += 1
    print(c, end=' ')


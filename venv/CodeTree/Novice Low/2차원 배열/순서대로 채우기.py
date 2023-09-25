n = 3
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]
# 첫 번째 행에 전부 숫자 1 채우기
for j in range(n):
    arr_2d[0][j] = 1

for i in range(1, n):
    for j in range(n):
        arr_2d[i][j] = arr_2d[i - 1][j] + 2

for row in arr_2d:
    for elem in row:
        print(elem, end=' ')
    print()
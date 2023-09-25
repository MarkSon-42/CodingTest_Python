import sys

n = int(input())
if n == 1:
    print(1)
    sys.exit()
if n == 2:
    print(1)
    print(1, 1)
    sys.exit()

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]
# 첫 번째 행에 전부 숫자 1 채우기
for i in range(n):
    arr_2d[i][0] = 1

for i in range(n):
    for j in range(i + 1):
        arr_2d[i][j] = arr_2d[i-1][j-1] + arr_2d[i-1][j]

for i in range(n):
    for j in range(i + 1):
        print(arr_2d[i][j], end=' ')
    print()
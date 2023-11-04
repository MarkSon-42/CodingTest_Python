n = 4
arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1

for i in range(n):
    if i % 2 == 0:  # 짝수일때는 정방향으로 += 1 하면서 배열 채우기
        for j in range(n):
            arr_2d[i][j] = num
            num += 1
    else:
        for j in range(n - 1, -1, -1):  # 홀수일때는 역방향으로 += 1 배열 채우기
            arr_2d[i][j] = num
            num += 1


for row in arr_2d:
    for elem in row:
        print(elem, end=' ')
    print()
# 문제
# 1이상 100이하의 수로만 이루어져 있는 n * n 크기의 격자 정보가 주어집니다. 이후 (r1, c1), (r2, c2) 값이 주어졌을 때, (r1, c1) 에서 (r2, c2) 내에 있는 수들의 최솟값을 출력하는 프로그램을 작성해보세요.
#
# 입력 형식
# 첫 번째 줄에는 n이 주어집니다.
# 두 번째 줄부터 n개의 줄에 걸쳐 각 행에 해당하는 n개의 숫자가 공백을 사이에 두고 주어집니다.
# n + 2번째 줄에는 구간의 시작 행과 열의 번호 (r1, c1) 값이 공백을 사이에 두고 주어집니다. n + 3번째 줄에는 구간의 끝 행과 열의 번호 (r2, c2) 값이 공백을 사이에 두고 주어집니다.
#
# 1 ≤ n ≤ 100
# 1 ≤ 주어지는 수 ≤ 100
# 1 ≤ r1 ≤ r2 ≤ n
# 1 ≤ c1 ≤ c2 ≤ n
# 출력 형식
# 첫 번째 줄에 주어진 구간 내의 숫자들의 최솟값을 출력합니다.
#
# 입출력 예제
# 예제1
# 입력:
#
# 4
# 1 4 3 2
# 5 2 3 1
# 3 2 4 1
# 1 1 1 1
# 2 3
# 4 4
# 출력:
#
# 1

#
# n = int(input())
# for _ in range(n):
#     maps = list(map(int, input().split()))
#
# r1, c1 = map(int, input().split())
# r2, c2 = map(int, input().split())
#
# maps_min = maps[r1][c1]
# for i in range(r1, c1):
#     for j in range(r2, c2):
#         if maps_min > maps[i][j]:

# gen by gpt

# Read input values
n, k = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

count = 0

for i in range(r1 - 1, r2):
    for j in range(c1 - 1, c2):
        if grid[i][j] >= k:
            count += 1

print(count)



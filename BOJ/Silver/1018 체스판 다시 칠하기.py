n, m = map(int, input().split())
plate = []

# 체스판 입력 받기
for _ in range(n):
    plate.append(input())

def count_changes(subplate):
    W_changes = 0
    B_changes = 0

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if subplate[i][j] != 'W':
                    W_changes += 1
                if subplate[i][j] != 'B':
                    B_changes += 1
            else:
                if subplate[i][j] != 'B':
                    W_changes += 1
                if subplate[i][j] != 'W':
                    B_changes += 1

    return min(W_changes, B_changes)

min_changes = float('inf')

# 8x8 체스판을 이동하면서 최소 변경 수 계산
for a in range(n - 7):
    for b in range(m - 7):
        subplate = [row[b:b+8] for row in plate[a:a+8]]
        changes = count_changes(subplate)
        min_changes = min(min_changes, changes)

print(min_changes)
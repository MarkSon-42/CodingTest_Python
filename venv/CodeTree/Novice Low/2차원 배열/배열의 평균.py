array = []
for _ in range(2):
    row = list(map(int, input().split()))
    array.append(row)

print(array)

row_avg = []
for row in array:
    avg = sum(row) / len(row)
    row_avg.append(avg)

col_avg = []
for j in range(4):
    column_sum = sum(array[i][j] for i in range(2))
    avg = column_sum / 2
    col_avg.append(avg)

total_avg = sum(row_avg) / len(row_avg)



# input
# 10 20 30 40
# 50 60 70 80

# output
# 25.0 65.0  행 평균
# 30.0 40.0 50.0 60.0  열 평균
# 45.0 전체 평균


# 두 배열의 같은 위치에 있는 숫자의 곱을 계산하여 결과 배열에 저장합니다.
for i in range(3):
    for j in range(3):
        result[i][j] = array1[i][j] * array2[i][j]

# 결과 배열을 출력합니다.
for row in result:
    print(row)
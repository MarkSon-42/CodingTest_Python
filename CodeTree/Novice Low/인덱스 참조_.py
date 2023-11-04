# 배열에서 홀수 번째 원소의 합 구하기
arr = list(map(int, input().split()))

n = len(arr)

sum_val = 0
for i in range(0, n, 2):  # 홀수 번째 인덱스 참조 range(0, n, 2)
    sum_val += arr[i]

print(sum_val)

#######################


# using slicing

slicing_num = list(map(int, input().split()))
filtered_arr = arr[::2]

sum_f = sum(filtered_arr)
print(sum_f)
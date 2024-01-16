#
# 1 5 2 6 8
#
# 2 5 2 6 8

n = int(input())

arr = [1, 5, 2, 6, 8]

answer = 0
for i in range(n):
    arr[i] *= 2

    sum_diff = 0
    for j in range(n - 1):
        sum_diff += abs(arr[j + 1] - arr[j])

    answer = max(answer, sum_diff)
    arr[i] //= 2  # 앞서 곱하기 한거 되돌려 두기

print(answer)

# 각 자리에 대해 상황을 일일이 가정해보고 진행해보는 완전탐색 방법


n = 5

arr = [-6, -5, -2, -10, -15]

max_val = 0

for i in range(n):
    if arr[i] > max_val:
        max_val = arr[i]

print(max_val)

# all elem neg, so...

# max_val 값의 초기값은, 들어올 수 있는 값들보다 훨씬 작은 값으로 잡기

import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

max_val = INT_MIN

for i in range(n):
    if arr[i] > max_val:
        max_val = arr[i]

print(max_val)

min_val = INT_MAX

for i in range(n):
    if arr[i] > min_val:
        min_val = arr[i]

print(min_val)

# 9,223,372,036,854,775,807
# 읽는 방법 : 구백이십이경 삼천삼백칠십이조 삼백육십팔억 오천사백칠십칠만 오천팔백칠

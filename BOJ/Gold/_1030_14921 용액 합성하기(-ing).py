# 각 용액 -100,000,000~ + _

# 특성 값 : 같은 양의 두 용액을 혼합하면, 그 특성값은 두 용액의 특성값의 합이 된다.

# 이분탐색

import sys
input = sys.stdin.readline

n = int(input())

solutions = list(map(int, input().split()))

left, right = 0, len(solutions) - 1

minval = 1e9  #  문제에서 주어진 조건 중 수의 범위가 10억 이내일 경우 사용 가능
# 1e9 = 1,000,000,000
# -1e9 = -1,000,000,000
while left < right:
    sum_sol = solutions[left] + solutions[right]
    if abs(sum_sol) < abs(minval):
        minval = sum_sol

    if sum_sol < 0:
        left += 1
    else:
        right -= 1
print(minval)
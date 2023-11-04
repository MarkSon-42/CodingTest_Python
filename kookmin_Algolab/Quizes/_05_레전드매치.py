# import sys
# input = sys.stdin.readline
answer = 0
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    nums = [int(x) for x in input().split()]
    for i in range(len(nums), 2): # 2개씩 봐야 하니까 이렇게>?
        if nums[i] == max(nums) and nums[i+1] == max(nums): # 최대값이 2개 이상이면,
            nums[i] += answer
            nums[i] = -1
        elif nums[i] == max(nums) and n > 0:
            nums[i] += answer
            n -= 1
        elif nums[i] == max(nums) and i == len(nums)-1:
            break
    print(answer)








# 권용재 학우님이 코드 _ 레전드 매치
import sys

t = int(input())
for tt in range(t):
    m, n = map(int, sys.stdin.readline().split())
    status = sorted(map(int, sys.stdin.readline().split()), reverse=True)
    if m % 2 != 0:
        status.append(0)
        m += 1
    delta = []
    for i in range(0, m, 2):
        temp = status[i] - status[i + 1]
        delta.append((i, temp))
    delta.sort(key=lambda x: x[1], reverse=True)

    for i in range(n):
        index = delta[i][0]
        status[index], status[index + 1] = status[index + 1], status[index]

    answer = 0
    for i in range(1, m, 2):
        answer += status[i]

    print(answer)

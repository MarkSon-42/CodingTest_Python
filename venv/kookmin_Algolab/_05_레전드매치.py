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







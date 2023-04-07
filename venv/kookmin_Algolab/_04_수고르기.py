# 이건 투포인터 문제야. 다시 풀어보자.

t = int(input())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    nums = list(map(int, input().split()))
    nums = nums.sort()
    for j in range(len(nums)-1, 0, -1):
        nums[j] - nums[]

# 두 수의 차이의 모든 경우의 수를 구하는 건가 ? 절대아닌듯
# 그러면 두 수의 차이중에 m미만인걸 어떻게 바로 걸러내나???




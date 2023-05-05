t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    diff = 1000000000
    for i in range(n - 1):
        for j in range(i+1, n):
            d = nums[j] - nums[i]
            if m <= d < diff:
                diff = d
                break
        if diff == m:
            break
    print(diff)


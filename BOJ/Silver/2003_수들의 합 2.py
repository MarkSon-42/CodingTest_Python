import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numarr = list(map(int, input().split()))
numarr.sort()
left, right = 0, 1
cnt = 0
while right <= n and left <= right:
    num_range = numarr[left:right]
    total = sum(num_range)

    if total == m:
        cnt += 1
        right += 1
    elif total < m:
        right += 1
    else:
        left += 1

print(cnt)

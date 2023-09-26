n = int(input())
nums = list(map(int, input().split()))

_list = [num ** 2 for num in nums]

for num in _list:
    print(num, end=' ')
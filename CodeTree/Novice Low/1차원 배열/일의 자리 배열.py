arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x, y = map(int, (input().split()))
arr[0] = x
arr[1] = y

for i in range(2, len(arr)):
    arr[i] = arr[i - 2] + arr[i - 1]
    while arr[i] > 9:
        arr[i] %= 10

for i in range(len(arr)):
    print(arr[i], end=' ')
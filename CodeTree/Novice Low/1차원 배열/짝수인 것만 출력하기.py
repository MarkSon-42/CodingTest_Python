n = int(input())
arr = list(map(int, input().split()))
new_arr = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        new_arr.append(arr[i])


for c in new_arr:
    print(c, end=' ')
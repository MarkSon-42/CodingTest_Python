arr = list(map(int, input().split()))
cnt = 0
mount = 0

for elem in arr:
    if elem == 0:
        break
    cnt += 1

arr = arr[:cnt]

sum_arr = []
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        sum_arr.append(arr[i])
        mount += 1
    else:
        continue

print(mount, sum(sum_arr))
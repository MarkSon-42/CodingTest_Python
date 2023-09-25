arr = list(map(int, input().split()))
cnt = 0

for elem in arr:
    if elem == 0:
        break
    cnt += 1

arr = arr[:cnt]

print(sum(arr), round(sum(arr)/cnt , 1))

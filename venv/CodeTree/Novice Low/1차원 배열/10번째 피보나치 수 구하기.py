arr = [0, 1, 1]

for i in range(3, 11):
    arr.append(arr[-1] + arr[-2])


    print(arr[10])


# fibo technic

ff, f = 1, 1
for _ in range(3, 11):
    ff, f = f, ff + f

print(f)
n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1

for i in range(n):
    num = 1
    num += i
    for j in range(n):
        print(num, end=' ')
        num += n
    print()



# 해설

n = int(input())

num = 1

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        ###############
        arr[j][i] = num
        ###############
        num += 1

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()
n = 4
arr_2d = [
    [0 for _ in range(n)
     for _ in range(n)]
]
print(arr_2d)

# list comprehension 사용시,
# n, m의 위치에 유의

n, m = 4, 5

arr_2d = [
    [0 for i in range(m)]
    for _ in range(n)
]


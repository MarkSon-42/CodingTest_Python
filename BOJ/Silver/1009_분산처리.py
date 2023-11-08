t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    data = a ** b

    print(data % 10)


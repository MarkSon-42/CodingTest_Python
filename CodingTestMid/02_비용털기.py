t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    num = list(map(int, input().split()))

    num.sort()
    a = 0
    b = n-1
    for _ in range(n):
        sum = num[a]+num[b]
        if (sum == p):
            print(num[a], num[b])
            break
        elif (sum < p):
            a += 1
        else:
            b -= 1
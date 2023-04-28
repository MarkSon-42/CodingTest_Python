t = int(input())
X = [-1, 1]

for i in range(t):
    n, m, d = map(int, input().split())
    data = [list(input()) for _ in range(m)]

    for j in range(len(data)-1, -1, -1):
        now_d = 2 * d - 2
        next_d = d
        for k in X:
            if 0 <= now_d + k < (2 * n - 1) and data[j][now_d+k] == '+':
                next_d = d + k
        d = next_d

    print(d)



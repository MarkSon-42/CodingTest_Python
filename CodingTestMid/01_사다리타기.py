numTestCase = int(input())
X = [1, -1]

for i in range(numTestCase):
    n, m, d = map(int, input().split())
    datas = []
    for j in range(m):
        datas.append(input())

    for j in range(len(datas)-1, -1, -1):
        now_d = (d + d - 1) - 1
        next_d = d
        for l in X:
            if 0 <= now_d + l < (2 * n - 1) and datas[j][now_d + l] == '+':
                next_d = d + l
        d = next_d
    print(d)
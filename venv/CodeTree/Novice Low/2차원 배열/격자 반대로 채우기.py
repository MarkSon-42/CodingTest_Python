n = int(input())
cnt = 1
answer = [[0 for _ in range(n)] for _ in range(n)]

if n % 2 != 0:
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i % 2 == 0:
                answer[j][i] = cnt
                cnt += 1
        for j in range(n):
            if i % 2 != 0:
                answer[j][i] = cnt
                cnt += 1

    for i in range(n):
        for j in range(n):
            print(answer[i][j], end=' ')
        print()

else:
    for k in range(n - 1, -1, -1):
        for l in range(n - 1, -1, -1):
            if k % 2 != 0:
                answer[l][k] = cnt
                cnt += 1
        for l in range(n):
            if k % 2 == 0:
                answer[l][k] = cnt
                cnt += 1
    for i in range(n):
        for j in range(n):
            print(answer[i][j], end=' ')
        print()


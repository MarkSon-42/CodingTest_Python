t = int(input())
for i in range(t):
    n = int(input())
    building = list(map(int, input().split()))
    v, answer = 0, 0
    for j in building[::-1]:
        if j > v:
            answer += 1
            v = j
    print(answer)

    
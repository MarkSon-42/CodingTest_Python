t = int(input())

X = [-1, 1]

for _ in range(t):
    n, m, d = map(int, input().split())
    datas = [list(input()) for _ in range(m)]

    now_d = 2 * d - 2

    for j in range(m-1, -1, -1): # m-1부터 0까지 역순으로 for루프를 반복.
        next_d = d
        for k in X: # 여기서, k가 -1일때와 1일때 각각 이동한 위치를 계산하여 next_d값을 업데이트 한다.
            if 0 <= now_d + k < ()
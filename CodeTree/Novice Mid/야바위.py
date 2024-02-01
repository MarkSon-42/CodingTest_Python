MAX_NUM = 3

n = int(input())
commands = [tuple(map(int, input().split())) for _ in range(n)]

max_score = 0

# 시작 위치를 전부 가정해보고 그 중 최대 점수 계산하기
# -> 완전탐색!

for i in range(1, 4):
    # 종이컵 전부 비워주기
    yabawi = [0] * 4

    # i번째 종이컵에 처음 조약돌 넣고 시작하기
    yabawi[i] = 1
    score = 0

    for a, b, c in commands:
        yabawi[a], yabawi[b] = yabawi[b], yabawi[a]

        if yabawi[c]:
            score += 1

    max_score = max(max_score, score)

print(max_score)

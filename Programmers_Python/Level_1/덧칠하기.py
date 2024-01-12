#  구역을 나누어 일부만 페인트를 새로 칠 함으로써 예산을 아끼려

# 각 구역에 왼쪽부터 순서대로 1번부터 n번까지 번호

# 롤러의 길이는 m미터

# 한 번 칠하는 규칙

#     롤러가 벽에서 벗어나면 안 됩

#     구역의 일부분만 포함되도록 칠하면 안 됩


# 롤러의 좌우측 끝을 구역의 경계선 혹은 벽의 좌우측 끝부분에 맞춘 후

# 롤러로 페인트칠을 하는 횟수를 최소화

# 알고리즘 없는 그냥 단순 구현문제

# 30분이 경과되었으나 풀이가 떠오르지 않음.

# 구현이 안되어 투포인터나 덱 모두 시도해봤으나 실패.


# def solution(n, m, section):
#     answer = 0
#     wall = [1 for _ in range(n)]
#     # 1 1 1 1 1 1 1 1
#     # 1 0 0 1 1 0 1 1
#     for i in range(0, len(section)):
#         if wall[section[i] - 1] == 1:
#             wall[section[i] - 1] = 0
#     # 벽을 만들고 안칠해진 상태까지 만들기
#
#     for i in range(n):
#         if wall[i] != 1:
#             for j in range(i, i + m):
#                 wall[j] = 1
#             i += m
#             answer += 1
#
#     return answer


def solution_2(n, m, section):
    answer = 1  # 칠하는 횟수
    paint = section[0]  # 덧칠 시작점
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]

    return answer


def solution_3(n, m, section):
    answer = 1
    prev = section[0]
    for sec in section:
        if sec - prev >= m:
            prev = sec
            answer += 1

    return answer


def solution_4(n, m, section):
    answer = 0
    # N 미터 벽
    # 페인트가 벗겨져 칠하기로함
    # 룰러의 길이 M
    #   - 구역의 일부부만 칠하기 안됨

    # Greedy

    coloredWall = 0
    for wall in section:
        if wall > coloredWall:
            coloredWall = wall + m - 1
            answer += 1
    return answer


def solution_5(n, m, section):
    answer = 1
    start = section[0]

    for i in section:
        if start + (m - 1) < i:
            answer += 1
            start = i

    return answer

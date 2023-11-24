# 맨해튼 거리가 2 이하
# -> 3~ 이상이어야 함!


# 얼마전에 푼 bfs문제가 아닐까
# 아기상어 2

# 'P'인지 아닌지 부터 검사하고
# 'P'이면 bfs를 호출?

# 그리고, 파티션을 고려해야.
# 파티션을 발견했다? -> 거리를 초기화 시켜주면 될것임..

# 아니, 근데 bfs필요가 없는게

# 그냥 'P'를 찾았으면, 맨하탄 디스턴스가 2이하이면 바로 false리턴하면 됨..


from collections import deque


def bfs(a, b, places):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((0, 0))
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and places[nx][ny] == "P":
                pass

    return 1


def solution(places):
    answer = []

    return answer

def solution(board):
    n = len(board)
    # 방향을 순차적으로 위에서부터 아래로
    direction_x = [-1, 0, 1, -1, 1, -1, 0, 1]
    direction_y = [-1, -1, -1, 0, 0, 1, 1, 1]

    # 지뢰가 설치된 곳
    booms = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                booms.append((x, y)) # 폭탄이 설치된 2차원 좌표 정보를 booms에 추가.

    for x, y in booms:
        for i in range(8):
            nx = x + direction_x[i]
            ny = y + direction_y[i]
            if 0 <= nx < n and 0 <= ny < n: # 지뢰 주변 폭탄 설치가 지도 범위 내에서 가능한지 체크
                board[nx][ny] = -1

    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1

    return answer




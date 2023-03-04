def solution(wallpaper):
    drag_start = [9999, 9999]  # 아주 큰 값을 넣어서 초기화 하는것은 대소비교에서 기본적인 테크닉이다. 최소를 구할때는 문제범위밖의 가장 큰값과 비교해서 갱신해주자.
    drag_end = [0, 0]  # 위와 같은 원리로.
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if drag_start[0] > i:
                    drag_start[0] = i  # 최소 x좌표를 넣어주는 코드
                if drag_start[1] > j:
                    drag_start[1] = j
                if drag_end[0] < i:
                    drag_end[0] = i
                if drag_end[1] < j:
                    drag_end[1] = j

    # 일단 첫점은 잘 뽑힌다.

    return drag_start[0], drag_start[1], drag_end[0] + 1, drag_end[1] + 1
    # end에 +1을 해줘야 한다. 왜냐하면 좌표는 직사각형의 꼭지점을 의미하는데, end에서 +1 해주지 않으면 이는 직사각형의 가장 왼쪽 상단 꼭지점을 의미하기 때문이다.
    # 그려보면 직관적으로 이해가 가능한 부분이다!


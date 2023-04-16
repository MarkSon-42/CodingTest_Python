# programmers lv.01

# 인물의 그리움 점수를 합산
# ma, ke ,ka _ 5 10 1 ... sum 16
# 그리움 점수가 없을 수 있음.


def solution(name ,yearing, photo):
    # name ~ yearing dict (python hash)
    n2y = {n:y for n, y in zip(name, yearing)}
    answer = []

    for pic in photo:
        pic_y = 0
        for person in pic:
            if person in name:
                pic_y += n2y[person]
        answer.append(pic_y)

    return answer
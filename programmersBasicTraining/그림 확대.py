def solution(picture, k):
    # 이미지 파일의 행과 열 크기 계산
    rows = len(picture)
    cols = len(picture[0])

    # k배 확대된 행과 열 크기 계산
    enlarged_rows = rows * k
    enlarged_cols = cols * k

    # 확대된 이미지 파일 생성
    enlarged_picture = []

    for row in picture:
        # 각 행을 k배 확대하여 새로운 행 생성
        enlarged_row = ''

        for pixel in row:
            # 각 픽셀을 k배 확대하여 새로운 픽셀 생성
            enlarged_pixel = pixel * k
            enlarged_row += enlarged_pixel

        # 새로운 행을 확대된 이미지 파일에 추가
        for _ in range(k):
            enlarged_picture.append(enlarged_row)

    # 확대된 이미지 파일 반환
    return enlarged_picture




def solution2(picture, k):
    answer = []
    for i in range(len(picture)):
        for _ in range(k):
            answer.append(picture[i].replace('.', '.' * k).replace('x', 'x' * k))

    return answer


# 내가 구현하길 원했던 풀이는 이 풀이인듯??
def solution3(picture, k):
    answer = []
    for i in picture:
        temp = ''
        for j in i:
            temp += j * k

        for _ in range(k):
            answer.append(temp)

    return answer

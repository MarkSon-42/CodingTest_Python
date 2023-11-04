def solution(myString):
    # "x"를 기준으로 문자열을 잘라서 배열 생성
    arr = myString.split("x")

    # 빈 문자열을 제외하고 알파벳순으로 정렬
    sorted_arr = sorted([s for s in arr if s])

    return sorted_arr

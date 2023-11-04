def solution(arr):
    # 2를 포함하는 부분 배열의 시작과 끝 인덱스
    start = -1
    end = -1

    # arr에서 2를 찾아 가장 작은 부분 배열을 구함
    for i in range(len(arr)):
        if arr[i] == 2:
            if start == -1:
                start = i
            end = i

    # 2를 포함하는 부분 배열이 없는 경우 [-1]을 반환
    if start == -1:
        return [-1]

    return arr[start:end+1]

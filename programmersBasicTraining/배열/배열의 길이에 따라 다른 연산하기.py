def solution(arr, n):
    new_arr = arr.copy()  # arr을 복사하여 새로운 배열 생성

    if len(arr) % 2 == 0:  # 배열의 길이가 짝수인 경우
        for i in range(1, len(arr), 2):  # 홀수 인덱스 위치에 접근
            new_arr[i] += n
    else:  # 배열의 길이가 홀수인 경우
        for i in range(0, len(arr), 2):  # 짝수 인덱스 위치에 접근
            new_arr[i] += n

    return new_arr

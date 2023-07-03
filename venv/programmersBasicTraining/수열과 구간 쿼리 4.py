def solution(arr, queries):
    for query in queries:  # 쿼리스 목록의 각 쿼리를 반복
        s, e, k = query  # 각 쿼리에 대해 시작 인덱스 s, 끝 인덱스 e, 및 값 k를 추출.
        for i in range(s, e + 1):  # 그런 다음 s에서 e범위를 반복하고
            if i % k == 0:  # 각 인덱스 i가 k의 배수인지 확인
                arr[i] += 1
    return arr

def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        sub_arr = arr[s:e+1]
        sub_arr.sort()
        found = False
        for num in sub_arr:
            if num > k:
                answer.append(num)
                found = True
                break
        if not found:
            answer.append(-1)
    return answer


import bisect



def solution2(arr, queries):
    answer = [-1] * len(queries)  # 결과를 저장할 배열을 미리 생성

    for idx, query in enumerate(queries):
        s, e, k = query
        sub_arr = sorted(arr[s:e + 1])  # 부분 배열을 정렬하여 사용

        # 이진 탐색을 사용하여 정렬된 배열에서 최소값보다 큰 첫 번째 요소의 인덱스를 찾음
        index = bisect.bisect_right(sub_arr, k)

        if index < len(sub_arr):  # 찾은 인덱스가 유효한 경우
            answer[idx] = sub_arr[index]

    return answer

def solution(arr, queries):
    for query in queries: # 쿼리스 목록의 각 쿼리를 반복
        s, e, k = query # 각 쿼리에 대해
        for i in range(s, e + 1):
            if i % k == 0:
                arr[i] += 1
    return arr

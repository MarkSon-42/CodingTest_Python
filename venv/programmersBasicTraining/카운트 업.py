def solution(start, end):
    answer = []
    sz = end - start + 1
    while sz > 0:
        answer.append(start)
        start += 1
        sz -= 1
    return answer
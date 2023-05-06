def solution(start, end):
    answer = []
    sz = start- end + 1
    while sz > 0:
        answer.append(start)
        start -= 1
        sz -= 1
    return answer
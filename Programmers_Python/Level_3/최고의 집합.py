def solution(n, s):
    answer = []

    if s < n:
        return -1
    for _ in range(n):
        answer.append(s // n)

    index = len(answer) - 1

    for i in range(s - sum(answer)):
        answer[index] += 1
        index -= 1

    return answer
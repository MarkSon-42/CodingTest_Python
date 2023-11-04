def solution(a, b):
    answer = 0
    for i in range(len(a)):
        dotp = a[i] * b[i]
        answer += dotp
    return answer
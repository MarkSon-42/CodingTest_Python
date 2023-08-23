def solution(A,B):
    answer = 0
    tmp = 0
    n = len(A)
    A.sort()
    B.sort()
    for i in range(0, n):
        tmp = A[i] * B[-i - 1]
        answer += tmp
    return answer
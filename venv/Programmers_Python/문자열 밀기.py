def solution(A, B):
    answer = 0
    flag = 0
    for i in range(len(A)):
        if A == B:
            answer = 0
            flag = 1
            break
        else:
            A = A[-1] + A[:len(A) - 1]
            print(A)
            answer += 1
            if A == B:
                flag = 1
                break
    if flag == 0:
        answer = -1
    return answer




############ GPT optimization

def solution2(A, B):
    if A == B:
        return 0
    n = len(A) # <- 이렇게 길이 변수르 빼주는 습관을 들여야 한다... 매우 중요.
    for i in range(n):
        if A == B:
            return i # ... wow
        A = A[-1] + A[:n-1]

    return -1
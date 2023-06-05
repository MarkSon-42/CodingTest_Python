def solution(n):
    cand = []
    x = 1
    while n > x:
        if n % x == 1:
            cand.append(x)
        x += 1
    answer = min(cand)
    return answer


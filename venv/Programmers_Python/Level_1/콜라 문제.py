def solution(a, b, n):
    answer = 0
    while n >= a:
        tmp = n % a
        n = (n // a) * b
        answer += n
        n += tmp
    return answer
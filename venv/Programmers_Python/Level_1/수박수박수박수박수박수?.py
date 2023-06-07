def solution(n):
    answer = ''
    word = "수박"
    if n % 2 == 0:
        word *= n//2
        answer += word
    else:
        word *= (n//2)
        answer += word
        answer += "수"
    return answer
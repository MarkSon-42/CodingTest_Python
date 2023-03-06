# upper()를 사용해서 풀어보자
# 공백을 기준으로 대문자로 변환
# 제발 종이없이 그냥 무지성 하드코딩 절대 하지마라 제발....   a4 말고 알고리즘 풀이용 노트를 꼭 살것 ㅇㅇㅋ????
def solution(s):
    answer = ''
    if s[0].isalpha():
        answer += s[0].upper()
    if s[0].isdigit():
        answer += s[0]

    for i in range(1, len(s)):
        if s[i - 1] == ' ' and s[i].isalpha():
            answer += s[i].upper()
        if s[i] == ' ':
            answer += ' '
        elif s[i - 1] != ' ' and s[i].islower():
            answer += s[i]
        elif s[i - 1].islower() and s[i].isupper():
            answer += s[i].lower()
    return answer
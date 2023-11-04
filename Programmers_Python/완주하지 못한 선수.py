# 원래 출처는 크로아티아 정보올림피아드 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3
# 데이터는 그리 크지 않다.
# 참가자 중에 동명이인이 있을 수 있다는 조건을 처리해야 한다. 분명 테스트케이스에 해당 케이스가 포함되어있을 것
# 따라서 participant에 completion이 있다면 1:1로 대응해서 삭제해주는 작업이 필요하다.
# 종이에 그려보니 규칙성 하나를 발견
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(participant) - 1):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[len(participant) - 1]


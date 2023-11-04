# while문에서 '3' in.. 을 사용하는 법을 몰랐다. 숙지해 두자
# '3'이 str(answer)안에 있는가? -> 특정 패턴이 있는지 없는지 검사할 때 쓰면 좋을것이다.
def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
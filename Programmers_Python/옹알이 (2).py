# 네가지 발음을 최대 한번씩만 사용해서 조합한 발음만 가능

# 문자열 처리, 구현에 대한 실력 부족으로 접근이 어려움

def solution(babbling):
    answer = 0
    for babble in babbling:  # babble은 문자열 하나
        while babble:  # 문자열이 ''이 아닌이상 True _ python while 참고
            if babble[:3] in ["aya", "woo"]:  # babble의 앞 3글자가 aya 혹은 woo이면
                babble = babble[3:]  # babble에서 앞에 3개 자르고 보겠다.
            elif babble[:2] in ["ye", "ma"]:
                babble = babble[2:]
            # 발음이 가능하면 while을 돌면서 빈 문자열이 출력될 것이다.
            else:
                break
            print(babble)
        if babble == "":
            answer += 1

    return answer

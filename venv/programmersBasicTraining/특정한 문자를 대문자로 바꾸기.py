def solution(my_string, alp):
    # 결과를 저장할 빈 문자열을 생성합니다.
    result = ""

    # 문자열 my_string을 순회하면서 각 문자를 확인합니다.
    for char in my_string:
        # 만약 현재 문자가 alp와 일치한다면,
        if char == alp:
            # 대문자로 변환하여 결과 문자열에 추가합니다.
            result += char.upper()
        else:
            # 일치하지 않는 경우에는 원래 문자 그대로 결과 문자열에 추가합니다.
            result += char

    # 결과 문자열을 반환합니다.
    return result

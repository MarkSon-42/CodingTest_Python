def solution(my_string, s, e):
    # 인덱스 s부터 e까지의 부분 문자열 추출
    substring = my_string[s:e + 1]

    # 부분 문자열을 반전하여 새로운 문자열 생성
    reversed_string = substring[::-1]

    # 반전된 문자열을 원래 문자열에 삽입하여 결과 반환
    result = my_string[:s] + reversed_string + my_string[e + 1:]
    return result



def solution2(my_string, s, e):
    return my_string[:s]+my_string[s:e+1][::-1]+my_string[e+1:]

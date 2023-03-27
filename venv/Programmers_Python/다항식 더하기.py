 # 실패한 풀이
 # def solution(polynomial):
 #    answer = ''
 #    x_num = 0
 #    num = 0
 #    for i in range(len(polynomial)):
 #        if int(polynomial[i]).isdigit() == True and polynomial[i+1] == 'x':
 #            x_num += int(polynomial[i])
 #        elif polynomial[i] == 'x' and polynomial[i+1] == ' ':
 #            x_num += 1
 #        else:
 #            if int(polynomial[i]).isdigit():
 #                num += int(polynomial[i])
 #
 #    return x_num + "x + " + num
 #
 #
 #    return answer



 # https://comdoc.tistory.com/entry/%EB%8B%A4%ED%95%AD%EC%8B%9D-%EB%8D%94%ED%95%98%EA%B8%B0

 # temp 리스트에 x항과 상수항을 각각 분리
 # 분리된 항의 계수의 합을 구함.
 # 각각의 항을 텍스트로 변환 후 기호를 넣어서 병합

 # 너무 복잡하지 않나..?

 # https://windy7271.tistory.com/305

 # 이 풀이를 참고

def solution(polynomial):
    x, num = 0, 0 # x, n은 각각 1차항계수, 상수 _ init
    polynomial = polynomial.split(" + ")
    for i in polynomial:
        if i.isnumeric(): # isnumeric() :  https://it-neicebee.tistory.com/33
            # return eval(polynomial) , python eval() : 문자열로 싯을 입력하면 해당식을 실행한 결과값으로 반환해줌.
            num += int(i)
        else:
            if len(i) == 1: # 문자열이 등장하면 길이를 이용한 테크닉을 생각해보기...
                x += 1
            else:
                x += int(i[:-1])

    if x == '0' and num == '0':
        return 0
    if x == '0':
        return num
    if x == '1':
        x = ""
    if num == '0':
        return x + "x"
    return x + "x + " + num
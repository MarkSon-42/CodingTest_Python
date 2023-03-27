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
    x, num = 0, 0
    polynomial = polynomial.split(" + ")
    for i in polynomial:
        if i.isnumeric(): # isnumeric() :  https://it-neicebee.tistory.com/33

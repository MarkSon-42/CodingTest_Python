# https://it-neicebee.tistory.com/33

# isdecimal()
#
# isdigit()
#
# isnumeric()
#
# => 셋다 주어진 문자열이 숫자로 되어있는지 검사하는 함수

a = '13524'

print(a.isdecimal())
print(a.isdigit())
print(a.isnumeric())


a = '3²' # 여기서 ²는 특수문자이다.

print(a.isdecimal())
print(a.isdigit())
print(a.isnumeric())

# 왜 그럴까?
# 3²에서 ²는 특수문자이지만 isdigit() 함수와 isnumeric() 함수로는 True가 반환된다.
#
# 하지만 isdecimal() 함수로는 False가 반환된다.
#
#
#
# 이것은 함수 차이인데 isdigit() 함수는 단일 글자가 '숫자' 모양으로 생겼으면 무조건 True를 반환하는 함수. 즉, 숫자처럼 생긴 '모든 글자'를 숫자로 친다.
#
# 그에 비해 isdecimal() 함수는 주어진 문자열이 int형으로 변환이 가능한지 알아내는 함수이기 때문에 특수문자 중 숫자모양을 숫자로 치지않는다.
#
#
#
# isnumeric() 함수는 숫자값 표현에 해당하는 문자열까지 인정한다. 제곱근 및 분수, 거듭제곱 특수문자도 isnumeric() 함수는 True를 반환하는 것을 알 수 있다.


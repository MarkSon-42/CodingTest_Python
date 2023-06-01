# 팰린드롬 6가지 방법

# 1. 문자열 뒤집기 _ 파이썬 슬라이싱
def pal_1(s):
    return s == s[::-1]

print(pal_1('refer'))

# 2. 양 끝에서부터 중앙으로 비교하기

def pal_2(s):
    for i in range(len(s) // 2): # 문자열의 중앙까지만 반복
        if s[i] != s[-1 -i]: # 앞뒤로 i번째 문자가 다르면
            return False
    return True

print(pal_1('stats'))

# 3. 문자열의 전처리
# 전처리? -> 원하는 작업을 수행하기 전에 데이터를 미리 처리하는 것

def pal_3(s):
    s = s.lower() # 모든 문자를 소문자로 변환
    s = s.replace(' ', '') # 모든 공백 제거
    return s == s[::-1]

print(pal_3('A man a plan a canal Panama'))


# 4. 스택 사용하기

def pal_4(s):
    s = s.lower().replace(' ', '') # 문자열 소문자, 공백제거 한번에
    stack = list(s)

    for char in s:
        if char != stack.pop():
            return False
    return True

print(pal_4('coffee'))


# 5. 데크를 사용한 최적화
from collections import deque

def pal_5(s):
    s = s.lower().replace(' ', '')
    deq = deque(s) # 데크 생성


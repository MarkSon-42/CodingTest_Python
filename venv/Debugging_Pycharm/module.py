c = 10

def mul(a, b):
    global c
    c += 1
    return a * b

# 내부 모듈 전역 변수인 c가 mul 함수가 실행되며 1이 증가한 것을 볼 수 있음.
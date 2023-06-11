def solution(a, b, c):
    if a != b and b != c and a != c:  # 세 숫자가 모두 다른 경우
        return a + b + c
    elif a == b == c:  # 세 숫자가 모두 같은 경우
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    else:  # 두 숫자가 같고 나머지 하나가 다른 경우
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)

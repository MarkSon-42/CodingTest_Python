# 소인수분해, 유클리드.. 또까묵
# math module 아마 시험때는 못쓸듯~ 그래도 알아두면 개꿀
from math import gcd

# Greatest Common Divisor
def solution(a, b):
    # 분모를 최대공약수로 약분하면 기약분수를 만들 수 있음
    b //= gcd(a, b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    return 1 if b == 1 else 2

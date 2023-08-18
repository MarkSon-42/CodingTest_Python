# 공배수 : 2개 이상 자연수의 공통된 배수
# LCM 최소공배수 : 그 중에 가장 작은 공배수

# 5의 배수 : 5, 10, 15, 20, 25, 30, ...
# 6의 배수 : 6, 12, 18, 24, 30, 36, ...
# 5와 6의 최소공배수 : 30, 60, 90 ...

# 어떤 2개 이상의 자연수의 공배수는 최소공배수의 배수이다.
# 최대 공약수는 공약수들만 곱하고, 최소공배수는 공약수에 서로소까지 곱한다.


# GCD
# 공통된 약수중에 가장 큰 수
# 8 : 1 2 4 8
# 10 : 1 2 5 10
# 공통 약수 1, 2   -> 가장 큰 공통 약수 2
# GCD : 2
#
# a = 10
# b = 12
# # GCD
# for i in range(min(a, b), 0, -1):  # range([a,b중 최소값 부터], 0직전까지(1까지) 역순으로])
#     if a % i == 0 and b % i == 0:
#         GCD = i
#         break
# # LCM
# for i in range(max(a, b), (a * b) + 1):
#     if i % a == 0 and i % b == 0:
#         LCM = i
#         break
#
#
# # 최대 공약수 구하기
#
# def solution(n, m):
#     GCD = 0
#     LCM = 0
#     # GCD
#     for i in range(min(a, b), 0, -1):  # range([a,b중 최소값 부터], 0직전까지(1까지) 역순으로])
#         if a % i == 0 and b % i == 0:
#             GCD = i
#             break
#     # LCM
#     for i in range(max(a, b), (a * b) + 1):
#         if i % a == 0 and i % b == 0:
#             LCM = i
#             break
#     return [GCD, LCM]
#
#
# # ver2

def solution2(n, m):
    gcd = lambda a,b : b if a % b == 0 else gcd(b, a % b)
    lcm = lambda a,b : a * b // gcd(a, b)
    return [gcd(n, m), lcm(n, m)]


solution2(256, 1836)


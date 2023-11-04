def solution(a, b):
    a_xor_b = int(str(a) + str(b))  # a ⊕ b의 값을 계산하여 a_xor_b에 저장합니다.
    double_a_b = 2 * a * b  # 2 * a * b의 값을 계산하여 double_a_b에 저장합니다.

    if a_xor_b == double_a_b:
        return a_xor_b
    elif a_xor_b > double_a_b:
        return a_xor_b
    else:
        return double_a_b


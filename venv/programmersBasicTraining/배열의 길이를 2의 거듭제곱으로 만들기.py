def solution(arr):
    n = len(arr)
    if n & (n - 1) == 0:  # 이미 2의 정수 제곱이면
        return arr
    else:
        next_power_of_2 = 2 ** (n.bit_length())
        zeros_to_add = next_power_of_2 - n
        return arr + [0] * zeros_to_add
def solution(number):
    if number == '0':
        return 0

    # 각 자릿수의 합 계산
    digit_sum = sum(int(digit) for digit in number)

    # number를 9로 나눈 나머지 계산
    remainder = digit_sum % 9

    return remainder

def solution2(my_string):
    answer = [0] * 52
    for x in my_string:
        if x.isupper():
            answer[ord(x) - 65] += 1
        else:

            answer[ord(x) - 71] += 1
    return answer
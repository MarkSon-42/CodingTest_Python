def multiply(arr):
    result = 1
    for number in arr:
        result *= number
    return result


def solution(num_list):
    if len(num_list) > 10:
        return sum(num_list)
    else:
        return multiply(num_list)

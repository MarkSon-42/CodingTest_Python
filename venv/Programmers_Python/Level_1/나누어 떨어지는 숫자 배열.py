def solution(arr, divisor):
    flag = 0
    answer = []
    for n in arr:
        if n % divisor == 0:
            answer.append(n)
            flag = 1
    answer.sort()
    return answer if flag == 1 else [-1]
def solution(numbers):
    answer = 0
    origins = [0,1,2,3,4,5,6,7,8,9]
    for i in range(len(origins)):
        if origins[i] not in numbers:
            answer += origins[i]
    return answer
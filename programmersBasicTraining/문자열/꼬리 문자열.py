def solution(str_list, ex):
    answer = ''
    for i in range(len(str_list)):
        if ex in str_list[i]:
            str_list[i] = ''
        answer += str_list[i]
    return answer
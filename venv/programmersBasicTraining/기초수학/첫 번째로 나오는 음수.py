def solution(num_list):
    flag = 0
    for i in range(len(num_list)):
        if num_list[i] < 0:
            flag = 1
            return i

    if flag == 0:
        return -1



def solution(num_list):
    num_plus = 0
    num_multi = 1
    for i in range(len(num_list)):
        num_plus += num_list[i]
        num_multi *= num_list[i]

    if num_plus * num_plus > num_multi:
        return 1
    else:
        return 0
def solution(num_list, n):
    return num_list[n:] + num_list[:n]  # 원하는 만큼 자르고 재배치

def solution(n_str):
    i = 0
    while n_str[i] == '0':  # 왼쪽에 연속으로 있는 0들을 찾음
        i += 1
    return n_str[i:]

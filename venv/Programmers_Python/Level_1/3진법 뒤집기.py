def solution(n):
    answer = ''

    while n > 0:  # 나중에 1을 3으로 나누면 몫이 0이되므로 while loop 탈출 가능
        n, re = divmod(n, 3)
        answer += str(re)
    return int(answer, 3)
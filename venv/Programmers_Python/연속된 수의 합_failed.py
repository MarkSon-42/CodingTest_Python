def solution(num, total):
    answer = []
    mid = 0
    dis = 0
    start = 0
    for i in range(num):
        if num % 2 != 0: # if num is odd
            # append for 문을 어떻게 만들지?
            # start, mid, end로 푸는게 아닌거 같은데?
            mid = total // num
            dis = num // 2
            start = mid - dis
            answer.append(start)
            start += 1
        else:
            pass
    return answer


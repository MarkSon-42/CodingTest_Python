def solution(num, total):
    mid = total // num
    half = num // 2
    top = mid + half + 1 # 연속된 수의 중간은 생각했는데 시작과 끝을                             변수로 두고 풀어낸다는 생각은 떠올리지 못했다.
    bot = top - num
    answer = [i for i in range(bot ,top)]
    return answer
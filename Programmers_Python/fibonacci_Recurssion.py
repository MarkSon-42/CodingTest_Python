# 이 코드도 동작하긴 하는데, run time error가 뜬다.
# 제한 사항에 n의 크기가 2 ~ 100,000까지 인데 재귀함수에서
def noF_Rec(n):
    answer = 0
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return noF_Rec(n - 1) + noF_Rec(n - 2)

    return answer
# # (0,0) (1,1) (2,2) (3,3) (4,4)... 에만 1이 들어감.
#
# # condition : if i == j:
#


def solution(n):
    answer = [[0] * n for _ in range(n)]
    for i in range(n):
        answer[i][i] = 1
    return answer
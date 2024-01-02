# def solution(d, budget):
#     answer = []
#     cnt = 0
#     while budget == 0:
#         for i in d:
#             budget -= i
#             cnt += 1
#             if budget < 0:
#                 continue
#             if budget == 0:
#                 answer.append(cnt)
#                 cnt = 0
#     return max(answer)
def solution(d, budget):
    answer = 0
    d = sorted(d)
    for dep in d:
        if budget - dep >= 0:
            answer += 1
            budget -= dep
        else:
            break

    return answer


def solution2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

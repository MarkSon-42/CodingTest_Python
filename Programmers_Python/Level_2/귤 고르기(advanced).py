import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)

    for value in sorted(cnt.values(), reverse=True):
        k -= value
        answer += 1
        if k <= 0:
            break
    return answer
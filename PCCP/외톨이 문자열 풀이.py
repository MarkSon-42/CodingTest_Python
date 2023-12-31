import collections


def solution(input_string):
    answer = ""
    sh = collections.defaultdict(int)
    prev = None  # null 객체임
    for cur in input_string:
        if cur != prev:
            sh[cur] += 1
        prev = cur

    for [key, val] in sh.items():
        if val > 1:
            answer += key

    if len(answer) == 0:
        return "N"

    return "".join(sorted(answer))

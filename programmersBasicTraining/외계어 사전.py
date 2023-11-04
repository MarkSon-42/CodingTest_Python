def solution(spell, dic):
    answer = 0
    for d in dic:
        cnt = 0
        for s in spell:
            if s in d:
                cnt += 1
        if cnt == len(spell):
            return 1
    return 2
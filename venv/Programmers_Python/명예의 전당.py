def solution(k, score):
    honor = []
    answer = []
    for i in range(len(score)):
        if len(honor) < k:
            honor.append(score[i])
            answer.append(min(honor))
            honor.sort()
        else:
            if score[i] >= max(honor):
                honor.append(score[i])
                honor.remove(min(honor))
                answer.append(min(honor))
            elif score[i] <= min(honor):
                answer.append(min(honor))
            elif score[i] >= min(honor) and score[i] <= max(honor):
                honor.append(score[i])
                honor.remove(min(honor))
                answer.append(min(honor))

    return answer
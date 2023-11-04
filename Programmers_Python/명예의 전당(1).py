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
            elif min(honor) <= score[i] <= max(honor):
                honor.append(score[i])
                honor.remove(min(honor))
                answer.append(min(honor))

    return answer

# 매우 안좋은 풀이로 반면교사 삼아서 업로드 하였음.
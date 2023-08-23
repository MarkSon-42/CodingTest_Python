def solution(k, tangerine):
    answer = 0
    dict1 = {}
    for i in tangerine:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    dict2 = sorted(dict1.items(), key=lambda x: -x[1])

    for i in dict2:
        if k <= 0:
            break
        else:
            k -= i[1]
            answer += 1
    return answer

solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
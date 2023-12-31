# 순서 훼손 안하면서 연속문자열은 중복 제외로 전처리 해버리기
# 그리고 2번이상 등장하면 외톨이 알파벳으로 편입


def solution(input_string):
    answer = []
    string = ""
    for i in range(1, len(input_string)):
        if input_string[i - 1] == input_string[i]:
            continue
        else:
            string += input_string[i - 1]

    string += input_string[-1]

    tmp = []
    # for c in string:
    #     if c not in tmp:
    #         tmp.append(c)
    #     else:
    #         continue

    for i in range(len(string)):
        if string.count(string[i]) > 1:
            answer.append(string[i])

    return "".join(sorted(list(set(answer)))) if len(answer) != 0 else "N"

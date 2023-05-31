def solution(str1, str2):
    l = len(str1)
    answer = ''
    for i in range(l):
        answer+=str1[i]
        answer+=str2[i]

    return answer
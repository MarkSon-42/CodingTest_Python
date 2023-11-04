def solution(answers):
    result = []
    temp_result = []
    cnt_1, cnt_2, cnt_3 = 0, 0, 0

    way_1st = [1, 2, 3, 4, 5]
    way_2nd = [2, 1, 2, 3, 2, 4, 2, 5]
    way_3rd = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        s1 = i % 5  # s1 = 0,1,2,3,4,0,1,2,3,4,...
        s2 = i % 8  # s2 = 0,1,2,3,4,5,6,7,0,1,2,3,4,5,,7,...
        s3 = i % 10  # s3 = 0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,...

        if way_1st[s1] == answers[i]:
            cnt_1 += 1
        if way_2nd[s2] == answers[i]:
            cnt_2 += 1
        if way_3rd[s3] == answers[i]:
            cnt_3 += 1

    k = max(cnt_1, cnt_2, cnt_3)

    if k == cnt_1:
        result.append(1)
    if k == cnt_2:
        result.append(2)
    if k == cnt_3:
        result.append(3)

    return result


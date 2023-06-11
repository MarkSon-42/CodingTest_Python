def solution(s):
    result = []
    last_occurrence = {}  # 각 문자의 마지막 등장 위치를 저장하는 딕셔너리

    for i, c in enumerate(s):
        if c in last_occurrence:
            result.append(i - last_occurrence[c])  # 마지막 등장 위치와의 거리를 결과에 추가
        else:
            result.append(-1)  # 동일한 문자가 없는 경우 -1을 결과에 추가

        last_occurrence[c] = i  # 현재 위치를 해당 문자의 마지막 등장 위치로 업데이트

    return result

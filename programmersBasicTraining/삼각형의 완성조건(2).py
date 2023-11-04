def solution(sides):
    answer = 0

    longest = max(sides)
    other = min(sides)
    for i in range(1, sum(sides) + 1):
        # 가장 긴 변이 max(sides)일 때
        if max(sides) < other + i and i < max(sides) + 1:
            answer += 1
        # 다른 한 변이 가장 긴 변일때
        if i < sum(sides) and i > max(sides):
            answer += 1
    return answer
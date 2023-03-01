# 순서를 바꿀 수 없기 때문에, card1은 yes, card2는 no

def solution(cards1, cards2, goal):
    answer = ''
    for i in range(len(goal)):
        if goal[i] == cards1[i]:
            del goal[i]
            del cards1[i]
        if goal[i] == cards2[i]:
            del goal[i]
            del cards2[i]

    if len(goal) > 0:
        return No
    else:
        return Yes
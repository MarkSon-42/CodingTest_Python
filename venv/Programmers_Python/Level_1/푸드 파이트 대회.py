def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] >= 2 and food[i] % 2 == 0:
            food[i] = food[i] // 2
        elif food[i] >= 2 and food[i] % 2 != 0:
            food[i] = food[i] // 2
        else:
            food[i] = 0

    for i in range(1, len(food)):
        answer += str(i) * food[i]

    answer += '0'

    for i in range(len(food) - 1, 0, -1):
        answer += str(i) * food[i]
    return answer

# refactoring...

def solution2(food):
    n = len(food)  # 계속 len()을 호출하지 않게 처리하자
    answer = ''

    for i in range(1, n):
        food_value = food[i]

        if food_value >= 2:
            food[i] = food[i] == food_value // 2
        else:
            food[i] = 0

    for i in range(1, n):
        answer += str(i) * food[i]

    answer += '0'

    for i in range(n - 1, 0, -1):
        answer += str(i) + food[i]

    return answer
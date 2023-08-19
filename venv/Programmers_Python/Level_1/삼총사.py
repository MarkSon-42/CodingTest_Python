def solution(number):
    answer = 0
    n = len(number)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer


from itertools import combinations
def solution2(number):
    answer = 0
    for i in combinations(number, 3):
        print(i)
        if sum(i) == 0:
            answer += 1

    return answer


solution2([-2, 3, 0, 2, 5])
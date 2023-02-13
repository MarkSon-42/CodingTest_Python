# 매개변수가 많아서 약간 복잡해 보이는 문제

# 기사단원의 수를 나타내는 정수 number
# 이웃나라와 협약으로 정해진 공격력의 제한수치를 나타내는 정수 limit
# 제한수치를 초과한 기사가 사용할 무기의 공격력을 나타내는 정수 power

# 1부터 number까지 약수의 개수를 구한다. [1, 2, 2, 3, 2]
# 해당 리스트를 돌면서, limit에 걸리면, power로 바꿔서 더해준다.
# 입출력 예시 2번을 보고 코드를 짜면 될 것이다.


def solution(number, limit, power):
    answer = 0
    for num in range(1, number + 1):
        weapon_power = 0
        for i in range(1, int(num ** 0.5) + 1): # 지난주에 다루었던 에라토스테네스의 체
            if num % i == 0:
                weapon_power += 1 # 약수의 개수가 무기의 공격력
                if i ** 2 != num: # 중복 방지 예를 들어, 25일 경우 1, 5, 25 -> 5 * 5 _  제곱 중복 방지
                    weapon_power += 1
            if weapon_power > limit:
                weapon_power = power
                break
        answer += weapon_power
    return answer
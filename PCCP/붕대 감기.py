def solution(bandage, health, attacks):
    answer = health
    idx = 0
    lastIdx = len(attacks) - 1
    consecutive = 0

    for time in range(1, attacks[lastIdx][0] + 1):
        if attacks[idx][0] == time:
            answer -= attacks[idx][1]
            idx += 1

            if answer <= 0:
                return -1

            consecutive = 0
            continue

        answer = min(answer + bandage[1], health)

        consecutive += 1

        if consecutive == bandage[0]:
            answer = min(answer + bandage[2], health)
            consecutive = 0

    return answer


# Example usage:
bandage = [2, 5, 7]
health = 20
attacks = [[1, 5], [3, 10], [5, 8], [7, 6]]
result = solution(bandage, health, attacks)
print(result)


def solution2(bandage, health, attacks):
    currentHealth = health  # 현재 체력
    success = 0  # 연속 성공
    attack = False
    bandageTime, recoveryBySecond, additionalRecovery = bandage

    attacksSecond = [attack[0] for attack in attacks]  # 공격을 받은 시간

    print(f"{0} {currentHealth} {success} {attack}")
    for second in range(1, attacksSecond[-1] + 1):
        if second in attacksSecond:  # 공격 받음
            attack = True
            success = 0  # 기술 취소
            currentHealth -= attacks[attacksSecond.index(second)][1]  # 공격 피해
        else:
            attack = False
            currentHealth += recoveryBySecond  # 초당 회복
            success += 1
            if success >= bandageTime:  # 연속 성공이면 추가 회복
                currentHealth += additionalRecovery
                success = 0
            if currentHealth > health:  # 최대 체력 보정
                currentHealth = health
        print(f"{second} {currentHealth} {success} {attack}")
        if currentHealth <= 0:
            return -1
    return currentHealth

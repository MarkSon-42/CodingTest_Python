from itertools import permutations


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    for i in range(1, len(numbers) + 1):
        perms = set(map(int, map("".join, permutations(numbers, i))))
        answer += sum(is_prime(n) for n in perms)

    return answer

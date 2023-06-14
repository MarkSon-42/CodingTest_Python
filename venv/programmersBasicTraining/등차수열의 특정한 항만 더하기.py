def solution(a, d, included):
    n = len(included)
    total = 0

    for i in range(n):
        if included[i]:
            term = a + (i * d)
            total += term

    return total
def solution(ineq, eq, n, m):
    if ineq == ">":
        if eq == "=":
            return int(n >= m)
        elif eq == "!":
            return int(n > m)
    elif ineq == "<":
        if eq == "=":
            return int(n <= m)
        elif eq == "!":
            return int(n < m)
    return 0


def solution2(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
def solution(n, lost, reserve):
    affordable = set(reserve) - set(lost)
    losted = set(lost) - set(reserve)
    for i in affordable:
        if i - 1 in losted:
            losted.remove(i-1)
        elif i + 1 in losted:
            losted.remove(i+1)

    print(n - len(losted))
    return n - len(losted)


solution(5, [2, 4], [1, 3, 5])


def solution2(n, lost, reserve):
    lost = set(lost)
    num_lost = len(lost)
    reserved = set(reserve) - set(lost)
    losted = set(lost) - set(reserve)

    for r in sorted(reserved):
        if r - 1 in losted:
            losted = losted - {r - 1}

        elif r + 1 in losted:
            losted = losted - {r + 1}

    return n - len(losted)
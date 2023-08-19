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
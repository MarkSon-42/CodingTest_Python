def solution(myString, pat):
    changed = ''
    for char in myString:
        if char == 'A':
            changed += 'B'
        else:
            changed += 'A'

    return 1 if pat in changed else 0
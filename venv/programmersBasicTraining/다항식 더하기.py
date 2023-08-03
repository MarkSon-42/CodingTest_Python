def solution(polynomial):
    x_number = 0
    const_number = 0

    for c in polynomial.split(' + '):
        if c.isdigit():
            const_number += int(c)
        else:r
            x_number = x_number + 1 if c == 'x' else x_number + int(c[:-1])

    if x_number == 0:
        return str(const_number)
    elif x_number == 1:
        return 'x + ' + str(const_number) if const_number != 0 else 'x'
    else:
        return f'{x_number}x + {const_number}' if const_number != 0 else f'{x_number}x'
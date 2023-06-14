def solution(quiz):
    result = []

    for formula in quiz:
        x, operator, y, _, z = formula.split()
        x = int(x)
        y = int(y)
        z = int(z)

        if operator == '+':
            if x + y == z:
                result.append('O')
            else:
                result.append('X')
        elif operator == '-':
            if x - y == z:
                result.append('O')
            else:
                result.append('X')

    return result

def solution(my_string, m, c):
    result = ""
    lines = [my_string[i:i + m] for i in range(0, len(my_string), m)]

    for line in lines:
        if len(line) >= c:
            result += line[c - 1]

    return result

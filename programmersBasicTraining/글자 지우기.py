def solution(my_string, indices):
    result = ''
    for i, char in enumerate(my_string):
        if i not in indices:
            result += char
    return result
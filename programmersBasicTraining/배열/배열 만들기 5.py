def solution(intStrs, k, s, l):
    result = []
    for string in intStrs:
        substring = string[s:s+l]
        converted = int(substring)
        if converted > k:
            result.append(converted)
    return result

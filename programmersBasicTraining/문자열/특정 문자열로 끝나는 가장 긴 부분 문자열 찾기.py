def solution(myString, pat):
    end = myString.rfind(pat)
    return myString[:end + len(pat)]


def solution2(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]
def solution(myString):
    answer = ''
    myString = list(myString)
    for i in range(len(myString)):
        if myString[i] == 'a' or myString[i] == 'A':
            myString[i] = 'A'
        else:
            myString[i] = myString[i].lower()

    answer = ''.join(s for s in myString)

    return answer

def solution2(myString):
    return myString.lower().replace('a', 'A')
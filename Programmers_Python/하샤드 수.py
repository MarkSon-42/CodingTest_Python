
def solution(x):
    arr = list(str(x))
    harshad = 0

    for i in range(len(arr)):
        harshad += int(arr[i])
        if x % harshad == 0:
            answer = True
        else:
            answer = False

    return answer
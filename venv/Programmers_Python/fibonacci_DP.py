FibArray = [0, 1]

def solution(n):
    if n < len(FibArray):
        return FibArray[n]
    else:
        FibArray.append(solution(n-1) + solution(n-2))
        return FibArray[n]


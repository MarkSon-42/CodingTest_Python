def solution(arr, flag):
    X = []
    for i in range(len(arr)):
        if flag[i]:
            X.extend([arr[i]] * 2)
        else:
            X = X[:-arr[i]]
    return X

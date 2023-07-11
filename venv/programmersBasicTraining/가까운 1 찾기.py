def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1

# 문제에 오류가 있다

# idx보다 크면서 -> idx와 크거나 같은
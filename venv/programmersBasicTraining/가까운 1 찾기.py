def solution(arr, idx):
    n = len(arr)

    for i in range(idx + 1, n):
        if arr[i] == 1:
            return i

    return -1

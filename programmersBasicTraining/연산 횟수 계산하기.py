def solution(arr1, arr2):
    sum1 = sum(arr1)  # arr1의 모든 요소의 합
    sum2 = sum(arr2)  # arr2의 모든 요소의 합

    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1
    elif sum1 < sum2:
        return -1
    elif sum1 > sum2:
        return 1
    else:
        return 0

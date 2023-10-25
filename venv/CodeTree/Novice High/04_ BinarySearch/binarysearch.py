def binarysearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(arr[mid])
            break
        elif arr[mid] > target:
            right = mid + 1
        else:
            left = mid - 1
    return -1


binarysearch([1, 2, 3, 4, 5, 6, 7, 8], 5)

def binarysearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print(arr[mid])
            break
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

        print(mid, left, right)
    return -1


binarysearch([2, 10, 12, 16, 19, 21, 23, 24, 28, 31], 28)
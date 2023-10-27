def upper_bound(arr, target):
    left, right, min_idx = 0, len(arr) - 1, len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
            min_idx = min(min_idx, mid)
        else:
            left = mid + 1

    return min_idx
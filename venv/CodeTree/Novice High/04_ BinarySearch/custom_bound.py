def custom_bound(arr, target):
    left, right, max_idx = 0, len(arr) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid = 1
            max_idx = max(max_idx, mid)
        else:
            right = mid + 1

    return max_idx
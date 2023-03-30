# 1. bubble sort : 그냥 무작정 인접 인덱스끼리 배교해서 순차적으로 비교 -> swap    *TC = O(N^^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 2. selection sort : index 첫번째부터 쭉 순차적으로 비교. 작은것 나오면 swap해주고 인덱스++      *TC = O(N^^2)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 3. insertion sort :             *TC = O(N^^2)
def insertion_sort(arr):
    n  = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

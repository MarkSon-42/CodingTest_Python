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

# 3. insertion sort :  이건 동작방식 한번 그려봐야 겠다.           *TC = O(N^^2)
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

# 4. merge sort : 구현의 동작에 재귀적 성질이 있음을 잘 이해하며 코드를 읽어보기   *TC = O(n log n)
# 정렬 알고리즘은 gif를 보면서 직관적인 이해를 하고 써보면서 한번 더 이해하는 것이 가장 좋다고 생각한다.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0 # index initalize
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


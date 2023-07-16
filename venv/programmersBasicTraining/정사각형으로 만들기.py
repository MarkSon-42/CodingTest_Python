def solution(arr):
    rows = len(arr)
    cols = len(arr[0])

    if rows > cols:
        for i in range(rows):
            while len(arr[i]) < rows:
                arr[i].append(0)
    elif rows < cols:
        while len(arr) < cols:
            arr.append([0] * cols)

    return arr
def solution(arr, queries):
    temp = 0
    print(len(queries))
    for i in range(len(queries)):
        temp = arr[queries[i][0]]
        arr[queries[i][0]] = arr[queries[i][1]]
        arr[queries[i][1]] = temp
    return arr



def solution2(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr
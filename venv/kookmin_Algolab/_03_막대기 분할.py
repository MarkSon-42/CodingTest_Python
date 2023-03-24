n = int(input())

for i in range(n):
    arr = list(input())
    lenA = len(arr)
    for j in range(lenA - 2):
        if arr[j] == '(' and arr[j+1] == ')':
            print(arr)


# ()은 레이저이다.
# ( ~ ) 은 막대기이다.
# 일단 레이저부터 반영해볼까?

# 너무 어렵다.
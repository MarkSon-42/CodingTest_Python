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

# 힌트 : 스택
# 스택 안써도 되긴 함

# 매번 할당량을 계산하는게 오버헤드가 너무 크다...
# sum()때문에
# 문제 잘못낸거 아님 ㅅㅂ....


# 이건 메모리문제는 아니고 시간 문제인데,
# python method들의 복잡도를 어느정도 알고 있어야 한다
# python에서 포인터 쓰는법 알아야 한다.
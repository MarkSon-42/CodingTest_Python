t = int(input())

for _ in range(t):
    n, p = map(int, input().split()) # 사용자로부터 입려받은 값을 split함수로 나누고,
    # map 함수를 이용하여 각 값들을 int형으로 변환한 뒤, n, p변수에 할당한다.

    num = list(map(int, input().split()))
    num.sort() # 오름차순으로 정렬
    a = 0 # two pointer (front)
    b = n-1 # two pointer (behind)
    for _ in range(n):
        sum = num[a] + num[b]
        if (sum == p):
            print(num[a], num[b])
            break
        elif (sum < p):
            a += 1
        else:
            b -= 1



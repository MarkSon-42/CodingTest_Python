t = int(input())
answer = 0
for i in range(t):
    n, p = map(int,input().split())

    if p % 2 == 0:
        answer = (n // 2) + 1
        print(answer)
    else:
        answer = n // 2
        print(answer)



# 아래 코드는 75점 (why??)
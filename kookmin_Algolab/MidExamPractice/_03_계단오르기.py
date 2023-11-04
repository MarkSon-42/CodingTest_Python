t = int(input()) # 테케 입력받고,

for _ in range(t): # 테스트케이스 수만큼 입력받기
    n, p = map(int, input().split()) # n과 p를 입력받기. n은 계단의 총 수 , p는 망가진 계단의 위치.

    if n % 2 == 0:
        if p % 2 == 0:
            print((n//2) + 1)
        else:
            print(n//2)
    else:
        print((n//2)+1)
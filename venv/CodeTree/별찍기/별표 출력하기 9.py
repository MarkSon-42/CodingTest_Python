n = int(input())
for i in range(n):
    for j in range(n+1 - 2*i + 1):   #  4  2  0  2씩 감소 -> 공백을 감소하면서 찍는다?
        # 앞에 입력값 n부터 박는다.
        # 루프 범위 : n값에서 i씩 줄이면서 출력 -> 역순에서 출력 -> 그래서 n - i 패턴이 나오는 것임!!
        print(' ', end = '')
    for k in range(2 * i + 1):
        print('*', end = ' ')
    print()
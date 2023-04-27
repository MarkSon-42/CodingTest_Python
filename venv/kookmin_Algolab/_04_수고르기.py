t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort() # 정렬을 해줘야 투포인터 적용이 의미가 있다.

    diff = 1000000000 # 1억으로 초기화. diff <- 이 변수는 차이의 최솟값을 나타낸다.
    for i in range(n - 1): # i 변수를 0 부터 n-2까지 반복문을 실행.
        for j in range(i+1, n): # j 변수를 i+1부터 n-1까지 반복문을 실행.
            d = nums[j] - nums[i] # 두 포인터가 가리키는 값의 차이를 d에 할당.
            if m <= d < diff: # 핵심 코드 : 차이가 m이상이고 diff보다 작은 경우를 비교.
                diff = d # 차이의 최소값 최신화.
                break
        if diff == m:
            break
    print(diff)

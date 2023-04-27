t = int(input())

for cnt in range(t): # 왜 증감 인덱스가 cnt인지??
    n = int(input())
    A, B = [], [] # 공장 A와 B에 주문한 제품 개수를 저장하는 리스트
    sum_a, sum_b = 0, 0 # 각각 가게에 주문한 총 개수를 저장

    for _ in range(n):
        a = input() # 처리해야할 주문
        if a[0] == 'O':
            ord, cnt, fac = a.split() # 공백을 기준으로 ord, cnt, fac 각각 할당
        else:
            ord, fac = a.split()

        if ord == "ORDER": # ORDER일 경우, fac(공장이름)과,  cnt(주문량) 파싱
            if fac == 'A': # 주문 할당 공장이 A인 경우
                A.append(int(cnt))
                sum_a += int(cnt)
            elif fac == 'B': # 주문 할당 공장이 B인 경우
                B.append(int(cnt))
                sum_b += int(cnt)
            else: # 주문 할당 공장이 C인 경우
                if sum_a <= sum_b:
                    A.append(int(cnt))
                    sum_a += int(cnt)
                else:
                    B.append(int(cnt))
                    sum_b += int(cnt)
        else:
            if fac == 'A':
                sum_a -= A.pop(0)
            else:
                sum_b -= B.pop(0)
    print(sum_a,sum_b)


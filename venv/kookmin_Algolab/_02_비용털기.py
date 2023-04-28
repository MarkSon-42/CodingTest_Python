t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    pc = list(map(int, input().split()))
    pc.sort()
    a = 0
    b = n - 1
    for _ in range(n):
        sum_pc = pc[a] + pc[b]
        if sum_pc == p:
            print(pc[a], pc[b])
            break
        elif sum_pc < p:
            a += 1  # a 증가 _ 인덱스
        else:
            b -= 1  # b 감소 _ 맨 오른쪽 큰 값을 가리키는 인덱스는 -=을 해줘야 한다!



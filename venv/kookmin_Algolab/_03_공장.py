from collections import deque
# 매번 남은 할당량을 계산하는 것은 오버헤드가 크다. 특히 파이썬

t = int(input())

for i in range(t):
    n  = int(input())
    A = 0
    B = 0
    factory = ''
    aloc = 0
    for j in range(n):
        msg = str(input())
        if len(msg) >= 9 and msg[-1] == 'C': # ORDER C
            if A <= B:
                A += int(msg[6])
            else:
                B += int(msg[6])




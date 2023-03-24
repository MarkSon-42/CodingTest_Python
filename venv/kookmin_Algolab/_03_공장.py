t = int(input())

for i in range(t):
    n  = int(input())
    A = []
    B = []
    factory = ''
    aloc = 0
    for j in range(n):
        msg = str(input())
        if msg[:5] == 'ORDER':

            aloc = int(msg[6])
            factory = msg[8]
            if factory == 'A':
                A.append(aloc)
            elif factory == 'B':
                B.append(aloc)
            else:
                if sum(A) <= sum(B):
                    A.append(aloc)
                else:
                    B.append(aloc)
                    # ORDER 처리 끝.
        else:
            factory = msg[5]
            if factory == 'A':
                del A[0]
            else:
                del B[0]

    print(sum(A), sum(B))


# 시간 초과가 뜨네...?
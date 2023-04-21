# B F R L

t = int(input())

for i in range(t):
    n = int(input())

    j_map = [list(input().strip()) for _ in range(n)]

    for n in j_map:
        print(''.join(map(str, n)))



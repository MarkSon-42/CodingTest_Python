t = int(input())

for _ in range(t):
    n = int(input())
    building_list = list(map(int, input().split()))
    v, answer = 0, 0
    for i in building_list[::-1]:
        if i > v:
            answer += 1
            v = i
    print(answer)
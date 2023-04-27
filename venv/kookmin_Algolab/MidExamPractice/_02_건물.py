t = int(input())

for _ in range(t):
    n = int(input())
    answer = 0
    check = 0
    building = list(map(int, input().split()))
    for i in range(len(building)):
        if check < building[-1]:
            answer += 1
            check = building[-1]
        building.pop(-1)
    print(answer)
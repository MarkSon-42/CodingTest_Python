t = int(input())

for _ in range(t):
    answer = 0
    check = 0
    building = list(map(int, input().split()))
    for i in range(len(building)):
        if check < building[-1]: # 맨 뒤 빌딩 높이부터 체크
            answer += 1 # 보이는 건물 하나 추가요~
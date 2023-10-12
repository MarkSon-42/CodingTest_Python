# 최소 정수 출력

import heapq

# 입력이 자연수 x라면, 배열에 자연수 x를 넣습니다.

# 입력이 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거합니다.

pq = []

n = int(input())

for _ in range(n):
    num = int(input())
    if len(pq) < 1 and num == 0:
        print(0)
    elif num == 0:
        print(pq[0])
        heapq.heappop(pq)
    else:
        heapq.heappush(pq, num)


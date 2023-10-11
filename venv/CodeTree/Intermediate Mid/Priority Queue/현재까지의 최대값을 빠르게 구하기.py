# [3, 6, 2, 6, 7, 7, 2] 와 같이 숫자들이 순서대로 주어졌을 때,
# 각각의 숫자가 주어질 때 마다 지금까지 주어진 숫자들 중
# 최댓값을 출력하는 프로그램을 작성해보세요.

# priority queue를 이용하면 최댓값을 찾는 과정을 O(logN)에 할 수 있습니다. 따라서 총 시간복잡도가 O(NlogN)이 됩니다.

# heapq는 기본적으로 min-heap이 때문에 최솟값을 구해줌

import heapq

pq = []
heapq.heappush(pq, 3)
heapq.heappush(pq, 5)

print(pq[0])

print(len(pq))  # pq 원소개수 조회

# heapq가 비어있는지 조회

pq_empty = []
heapq.heappush(pq_empty, 5)
if pq_empty:  # 원소가 남아있다면
    print(pq[0])  # 최솟값을 출력


arr = [3, 6, 2, 6, 7, 7, 2]
pq = []

for elem in arr:
    heapq.heappush(pq, -elem)  # -를 붙여서 넣어준다
    print(-pq[0], end=' ')  # -한번 더 붙여줘서 출력한다



import heapq

n, m = map(int, input().split())
arr = list(map(int, input().split()))
pq = []

# priority queue에 숫자 넣어주기.
# 최대값을 구해야 하므로 미리 - 붙여서 넣어준다.

for elem in arr:
    heapq.heappush(pq, -elem)

    # m번에 걸쳐 최댓값을 찾아 1씩 빼주는 것을 반복

for _ in range(m):
    max_val = -heapq.heappop(pq)

    heapq.heappush(pq, -(max_val - 1))

print(-heapq.heappop(pq))

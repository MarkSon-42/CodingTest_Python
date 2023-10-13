import heapq

n, m = tuple(map(int, input().split()))

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

pq = []

# pq에 x + y, x, y 순으로 우선순위 되도록 : minheap

for x, y in points:
    heapq.heappush(pq, (x + y, x, y))

# print(pq)

for _ in range(m):
    _, x, y = heapq.heappop(pq)

    x, y = x + 2, y + 2
    heapq.heappush(pq, (x + y, x, y))

_, last_x, last_y = heapq.heappop(pq)
print(last_x, last_y)


import heapq

pq = []

# Adding elements to the queue with their priorities
heapq.heappush(pq, (5, "A"))
heapq.heappush(pq, (2, "B"))
heapq.heappush(pq, (7, "C"))
heapq.heappush(pq, (1, "D"))

while len(pq) > 0:
    element = heapq.heappop(pq)

    priority = element[0]
    value = element[1]

    print(f"{value} (priority: {priority}")


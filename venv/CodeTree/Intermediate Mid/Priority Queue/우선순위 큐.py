import heapq


class PriorityQueue:
    def __init__(self):  # 빈 Priority Queue 하나를 생성합니다.
        self.items = []

    def push(self, item):  # 우선순위 큐에 데이터를 추가합니다.
        heapq.heappush(self.items, -item)

    def empty(self):  # 우선순위 큐가 비어있으면 True를 반환합니다.
        return not self.items

    def size(self):  # 우선순위 큐에 있는 데이터 수를 반환합니다.
        return len(self.items)

    def pop(self):  # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터를 반환하고 제거합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")

        return -heapq.heappop(self.items)

    def top(self):  # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터를 제거하지 않고 반환합니다.
        if self.empty():
            raise Exception("PriorityQueue is empty")

        return -self.items[0]


pq = PriorityQueue()  # 우선순위 큐를 선언합니다. => 빈 우선순위 큐
pq.push(2)
pq.push(9)
pq.push(5)

print(pq.top())  # 최댓값을 출력합니다. => 9
pq.pop()  # 최댓값을 제거합니다.
print(pq.size())  # 원소의 개수를 출력합니다 => 2
while not pq.empty():  # 최댓값을 갖는 원소부터 순서대로 출력합니다.
    print(pq.top())  # 순서대로 5 2가 출력됩니다.
    pq.pop()  # 최댓값에 해당하는 원소를 뺍니다.


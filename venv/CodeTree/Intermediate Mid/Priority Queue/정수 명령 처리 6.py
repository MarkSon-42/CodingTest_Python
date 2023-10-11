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

n = int(input())
pq = PriorityQueue()  # 빈 우선순위 큐 선언

for _ in range(n):
    command = input()
    if command.startswith('push'):
        x = int(command.split()[1])
        #  이 줄은 입력된 command 문자열을 공백을 기준으로 분할하고,
        #  그 결과를 리스트로 반환합니다.
        #  그리고 그 리스트의 두 번째 항목(인덱스 1)을 정수로 변환하여 x에 할당합니다.
        #  이 부분은 사용자가 "push" 뒤에 어떤 값을 큐에 추가하고자 하는지를 파싱하는 부분입니다.

        pq.push(x)
    elif command == 'pop':
        print(pq.pop())
    elif command == 'size':
        print(pq.size())
    elif command == 'empty':
        print(1 if pq.empty() else 0)
    else:
        print(pq.top())


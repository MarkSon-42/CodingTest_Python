import heapq

lst = [5, 7, 9, 1, 3]


# heapq method... heapify()
# onvert the iterable into a heap data structure.
heapq.heapify(lst)

print("Cretead heap : ", (list(lst)))

heap_list = []
heapq.heappush(heap_list, 4)
heapq.heappush(heap_list, 1)
heapq.heappush(heap_list, 2)
heapq.heappush(heap_list, 5)
heapq.heappush(heap_list, 8)

# heappop()
heapq.heappop(heap_list)

# pop하지 않고 최솟값 얻기
print(heap_list[0])

# 기존 리스트를 힙으로 변환
a_list = [4, 1, 7, 3, 8, 5]
heapq.heapify(a_list)


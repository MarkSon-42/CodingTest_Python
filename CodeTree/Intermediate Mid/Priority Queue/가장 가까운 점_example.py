import heapq

points = [
    (1, 7), (3, 2), (3, 1), (6, 2)
]
pq = []

for point in points:
    x, y = point
    heapq.heappush(pq, (-x, -y)) # priority queue에 넣어줍니다.
                          # 단, x, y 모두 큰 값이 먼저 나오기를 원하므로
                          # -를 붙여서 넣어줍니다.

    best_point = pq[0]    # x, y 순으로 가장 우선순위가 높은 경우를 찾아줍니다.
    best_x, best_y = best_point

    print(-best_x, -best_y) # -를 붙여서 이용했으므로 사용할 때에는 다시 -를 꼭 붙여줘야 합니다.


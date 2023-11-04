import heapq


def solution(n, works):
    # 파이썬에서 heapq는 min-heap이므로, max-heap을 만들기 위해 works의 부호를 바꿔서 삽입합니다.
    works = [-work for work in works]
    heapq.heapify(works)  # 리스트를 heap으로 변환합니다.

    # 가장 많은 시간이 남아 있는 작업을 반복적으로 선택합니다.
    for _ in range(n):
        # heap의 맨 위 요소를 선택합니다.
        work = heapq.heappop(works)
        if work == 0:  # 남아 있는 작업이 없다면, 중단합니다.
            break
        # 한 시간 작업한 후 다시 heap에 삽입합니다.
        heapq.heappush(works, work + 1)

    # 초과 근무 피로도를 계산합니다.
    overtime_fatigue = sum(work ** 2 for work in works)

    return overtime_fatigue  # 시작할 때 works의 부호를 바꾸었으므로, 결과 역시 부호를 바꿔줍니다.


# level 3 .. 못풀어서 gpt


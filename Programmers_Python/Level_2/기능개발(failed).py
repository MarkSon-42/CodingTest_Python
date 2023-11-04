from collections import deque


def solution(progresses, speeds):
    answer = []
    i = 0
    while progresses:
        if progresses[i] >= 100:
            progresses.popleft()
            i += 1
        else:
            progresses[i] += speeds[i]

    return answer

# ... ? 
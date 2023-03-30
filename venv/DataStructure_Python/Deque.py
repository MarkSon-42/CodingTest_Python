# Dequq.. 큐 자료구조인데, 양방향 큐이다.

# 앞, 뒤 방향에서 element 추가, 제거 가능하다.

# list는 위 연산에 O(1)이 걸리는데, dequq는 O(1)로 가능하다.

from collections import deque

deq = deque()

# Add element to the start(left)
deq.appendleft(10)

deq.append(0)

deq.popleft()

deq.pop()

# 데크(deque)에 존재하는 메서드(method)는 대략 다음과 같다.
#
# deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
# deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
# deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
# deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
# deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
# deque.remove(item): item을 데크에서 찾아 삭제한다.
# deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

# rotate()에 대한 설명

# Contain 1,2,3,4,5 in deq

deq = deq([1, 2, 3, 4, 5])

deq.rotate(1)
print(deq)
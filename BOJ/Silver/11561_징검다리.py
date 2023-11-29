# n개 징검다리

# 더 긴거리를 뛰어야 하고
# n번은 반드시 밟아야 함 ( 마지막 징검다리는 꼭 밟아야 한다는 뜻 )

# 범위가 10^16인걸 보고 이분탐색을 의심 그러나

# 이분탐색 연습이 너무 안되어 있음.

# 밟을 수 있는 징검다리 최대 수

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

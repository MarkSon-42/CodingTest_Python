import random

def random_path(start, end, graph):
    path  = [start]
    current = start
    while current != end:
        neighbors = graph[current]
        next_node = random.choice(neighbors)
        path.append(next_node)
        current = next_node
    return path

# 시작지점에서부터 무작위로 이동하여 도착점에 도달하는 경로를 찾는 알고리즘


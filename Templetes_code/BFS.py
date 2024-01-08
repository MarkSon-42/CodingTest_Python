from collections import deque

# Assuming VERTICES_NUM, graph, and visited are defined before calling BFS function


def BFS():
    # Initialize an empty queue
    q = deque()

    # Search for the first element until the queue is empty
    while q:
        curr_v = q.popleft()

        for next_v in range(1, VERTICES_NUM + 1):
            # If connected but not visited -> Determine conditions
            if graph[curr_v][next_v] and not visited[next_v]:
                print(next_v)
                visited[next_v] = True
                q.append(next_v)


# Sample usage:
# Initialize VERTICES_NUM, graph, and visited before calling BFS function
# For example:
# VERTICES_NUM = 5
# graph = [[0] * (VERTICES_NUM + 1) for _ in range(VERTICES_NUM + 1)]
# visited = [False] * (VERTICES_NUM + 1)
# q = deque()
# Add edges to the graph
# Call BFS function

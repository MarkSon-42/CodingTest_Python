graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

# 리스트(스택, 큐)를 이용한 DFS 구현

def dfs(graph, start_node):

    # 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, already_visited = list(), list()

    # 시작 노드를 정하기
    need_visited.append(start_node)

    # 만약 방문이 필요한 노드가 있다면,
    while need_visited:
        # 그 중에서 가장 마지막 데이터 추출 ( 스택 구조 활용 )
        node = need_visited.pop()

        # 만약 그 노드가 방문 목록에 없다면
        if node not in already_visited:

            already_visited.append(node)

            need_visited.extend(graph[node])
    return already_visited

dfs(graph, 'A')

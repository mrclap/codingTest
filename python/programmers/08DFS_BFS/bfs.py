'''
BFS
그래프의 모든 노드를 방문하고자 할 때,
원하는 결과를 얻어낼때까지 각 노드를 최소 한 번 이상 방문
'''


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n]

    return visited


if __name__ == '__main__':
    # undirected graph
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']}
    print(bfs(graph, 'A'))
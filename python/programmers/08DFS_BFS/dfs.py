'''
DFS는 한 번 선택한 길을 끝까지 판 뒤에 다음 길로 간다.
참.. 대단한 녀석이다...
'''

# with stack
def dfs(graph, start):
    stack = [start]
    visited = []

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n]

    return visited


# with recursive
def dfs_recursive_first(graph, start):
    visited = [start]
    for n in graph[start]:
        if n not in visited:
            dfs_recursive(graph, n, visited)

    return visited


def dfs_recursive(graph, node, visited):
    visited.append(node)
    for n in graph[node]:
        if n not in visited:
            dfs_recursive(graph, n, visited)


if __name__ == '__main__':
    # undirected graph
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']}
    print(dfs(graph, 'A'))
    print(dfs_recursive_first(graph, 'A'))
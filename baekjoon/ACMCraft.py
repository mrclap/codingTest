import sys

def solution():
    test_cases = sys.stdin.readline()
    for test_case in test_cases:
        num_of_bldg = 0
        num_of_rule = 0
        construct_time = dict()
        adj_dict = dict()
        target_bldg = 0

        [num_of_bldg, num_of_rule] = map(int, sys.stdin.readline().split())
        construct_time = {idx+1: e for idx, e in enumerate(map(int, sys.stdin.readline().split()))}
        adj_dict = {i+1: list() for i in range(num_of_bldg)}

        for i in range(num_of_rule):
            [start, end] = map(int, sys.stdin.readline().split())
            adj_dict[start].append(end)

        target_bldg = int(sys.stdin.readline())

        print(dfs(adj=adj_dict, start=1))

'''
def dfs(adj, start):
    visited = list()
    parent = dict()
    stack = list()

    stack.append(start)

    while len(stack) != 0:
        v = stack.pop()
        visited.append(v)
        for e in adj[v]:
            if e not in visited:
                dfs_visit(adj, e, visited, parent)

    return visited


def dfs_visit(adj, v, visited, parent):

    for e in adj[v]:
'''


# with recursive
def dfs(adj, start):
    visited = list()
    finished = list()
    dfs_visit(adj, start, visited, finished)
    return visited


def dfs_visit(adj, v, visited, finished):
    visited.append(v)
    for u in adj[v]:
        if u not in visited:
            dfs_visit(adj, u, visited)
        elif u not in finished:
            cycle = True
    finished.append(u)




# without recursive
def dfs_without_recursive(adj, start):
    visited = list()
    stack = [start]

    while stack:
        n = stack.pop()
        visited.append(n)
        for v in adj[n]:
            if v not in visited:
                stack.append(v)

    return visited









# def bfs(adj, start):
#     visited = []
#     queue = [start]
#     accumulated_construct_time = {}
#
#     while queue:
#         n = queue.pop(0)
#         if n not in visited:
#             visited.append(n)
#
#             for adj_node in adj[n]:
#                 if adj_node not in visited:
#                     queue.append(adj_node)
#
#     return visited


if __name__ == '__main__':
    solution()

'''
2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7
'''
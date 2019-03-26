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
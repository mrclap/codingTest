import sys

def solution():
    test_cases = int(sys.stdin.readline())
    answer = list()
    for i in range(test_cases):
        total_construct_time = dict()

        [num_of_bldg, num_of_rule] = map(int, sys.stdin.readline().split())
        construct_time = {idx+1: e for idx, e in enumerate(map(int, sys.stdin.readline().split()))}
        adj_dict = {i+1: list() for i in range(num_of_bldg)}

        for i in range(num_of_rule):
            [start, end] = map(int, sys.stdin.readline().split())
            adj_dict[start].append(end)

        target_bldg = int(sys.stdin.readline())

        for n in adj_dict:
            if n not in adj_dict.values():
                total_construct_time[n] = construct_time[n]

        topology = dfs(adj=adj_dict, start=1)
        assign_construct_time_each_bldg(adj_dict, topology, construct_time, total_construct_time)

        answer.append(total_construct_time[target_bldg])

    for each in answer:
        print(each)

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

def assign_construct_time_each_bldg(adj, topology, time_dict, total_time_dict):
    for v in topology:
        for u in adj[v]:
            total_time_dict[u] = max(total_time_dict[v] + time_dict[u], total_time_dict[u])
    return total_time_dict

# with recursive
def dfs(adj, start):
    visited = list()
    finished = list()
    dfs_visit(adj, start, visited, finished)
    finished.reverse()
    return finished
    # return visited


def dfs_visit(adj, v, visited, finished):
    visited.append(v)
    for u in adj[v]:
        if u not in visited:
            dfs_visit(adj, u, visited, finished)
        elif u not in finished:
            cycle = True
    finished.append(v)


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


'''
build_order = {}
build_time = []
answer_list = []
def main():
    global build_order
    global build_time
    case = int(input())
    for idx in range(case):
        row = input().split(" ")[1]
        build_time = input().split(" ")
        for jdx in range(int(row)):
            order = input().split(" ")
            start = str(order[0])
            end = str(order[1])
            if not build_order.get(end):
                build_order[end] = {}
                build_order[end]["parent"] = [start]
            else:
                if start not in build_order[end]["parent"]:
                    build_order[end]["parent"].append(start)

        target = input()

        answer_list.append(max_time(target))
        build_order = {}
        build_time = []

    for answer in answer_list:
        print(answer)


def max_time(build_number):
    global build_order
    global build_time

    self_dict = build_order.get(build_number)
    if not self_dict:
        return int(build_time[int(build_number) - 1])
    else:
        if self_dict.get("maxtime"):
            return self_dict.get("maxtime")

        else:
            mt = 0
            for parent in self_dict["parent"]:
                mt = max(mt,max_time(parent))

        mt = mt + int(build_time[int(build_number) - 1])
        self_dict["maxtime"] = mt
        return mt


if __name__ == "__main__":
    main()
'''
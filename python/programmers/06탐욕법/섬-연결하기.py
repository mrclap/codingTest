import unittest

'''
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제약조건 
    섬의 개수 n은 1 이상 100 이하입니다.
    costs의 길이는 ((n-1) * n) / 2이하입니다.
    임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
    같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
    모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
    연결할 수 없는 섬은 주어지지 않습니다.
'''

'''
8/27 1차 시도
    1) 주어진 못생긴 costs를 연결된 섬들을 바로 index에서 알 수 있도록 이차원 배열로 다시 mapping
    2) 아무 노드에서나 시작하고,
        노드가 연결할 수 있는 경로중에서 가장 작은 녀석을 선택해서 연결하며, 연결되었으면 연결드 list에 이름 넣고
        연결드 list에 있는 모든 노드 중 연결드list와 다시 연결되지 않는 경로중 가장 싼 노드와 또 연결
    성공!
'''


def solution(n, costs):
    answer = 0
    e = [[999_999_999 for c in range(n)] for r in range(n)]

    # 이차원 배열 매핑
    for cost in costs:
        row = cost[0]
        col = cost[1]
        c = cost[2]

        e[row][col] = c
        e[col][row] = c

    visited = [0]

    while True:
        local_min = 999_999_999
        local_min_idx = -1
        for node in visited:
            for idx in range(len(e[node])):
                if e[node][idx] < local_min and idx not in visited:
                    local_min = e[node][idx]
                    local_min_idx = idx
        visited.append(local_min_idx)
        answer += local_min
        if len(visited) == n:
            return answer

    return 'error'


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]), 4)


if __name__ == '__main__':
    unittest.main()
    # print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
    # print(solution("1924", 2))
    # print(solution("1231234", 3))
    # print(solution("111133255", 2))




import unittest

'''
두 개의 단어 begin, target과 단어의 집합 words가 있습니다.
아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.


예를 들어 begin이 hit, target가 cog, words가 [hot,dot,dog,lot,log,cog]라면
hit -> hot -> dot -> dog -> cog와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때,
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

제약조건 
    각 단어는 알파벳 소문자로만 이루어져 있습니다.
    각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
    words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
    begin과 target은 같지 않습니다.
    변환할 수 없는 경우에는 0를 return 합니다.

'''

'''
9/4 시도1
접근법
    begin을 시작으로, target을 목적지로하며 words를 노드로 하는 non-directed 그래프에 대해 최단경로(다익스트라)알고리즘을 수행하여 
    구하면 될 것 같다 결국은 완전 탐색이 될 거 같다
       
결과
    
'''
INF = 1_000_000_000


def solution(begin, target, words):
    answer = 0

    nodes = [begin] + words  # node[0] = start
    edges = [[True if row == col else False for row in range(len(nodes))] for col in range(len(nodes))]

    target_idx = -1
    # 1. graph 생성( adjacent_matrix )
        # start - begin
        # destination - target

    for idx in range(len(nodes)):
        if nodes[idx] == target:
            target_idx = idx
        ref = nodes[idx]
        for jdx in range(idx+1, len(nodes)):
            comp = nodes[jdx]
            count = 0
            for kdx in range(len(begin)):
                if ref[kdx] != comp[kdx]:
                    count += 1
            if count <= 1:
                edges[idx][jdx] = True
                edges[jdx][idx] = True

    if target_idx == -1:
        return 0

    # 2. 다익스트라

    start = 0
    visited = {idx: False for idx in range(len(nodes))}
    visited[0] = True
    steps = [1 if edge else INF for edge in edges[start]]
    steps[0] = 0

    idx = start

    for _ in range(len(nodes)-2):
        for adj_idx in range(len(edges[idx])):
            if edges[idx][adj_idx] and not visited[adj_idx]:
                idx = adj_idx
                break
        visited[idx] = True
        for adj_idx in range(len(edges[idx])):
            if edges[idx][adj_idx]:
                if steps[idx] + 1 < steps[adj_idx]:
                    steps[adj_idx] = steps[idx] + 1

    return steps[target_idx]


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']), 4)
        self.assertEqual(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']), 0)


if __name__ == '__main__':
    unittest.main()

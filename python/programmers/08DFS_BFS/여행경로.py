import unittest

'''
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때,
방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제약조건 
    모든 공항은 알파벳 대문자 3글자로 이루어집니다.
    주어진 공항 수는 3개 이상 10,000개 이하입니다.
    tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
    주어진 항공권은 모두 사용해야 합니다.
    만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
    모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

'''

'''
9/5 시도3
접근법
    처음부터 다시...!!! 모든 경우의 수에 대해 DFS로 ... 찾되, sort를 통해서
    DFS가 모든 티켓을 소진하게되는 첫번째 경우가 답이 되도록 해보자.
결과
    성공!
'''


def solution(tickets):
    adj = {}

    for ticket in tickets:
        start = ticket[0]
        destination = ticket[1]

        # making adjacent list
        if adj.get(start):
            adj[start].append(destination)
        else:
            adj[start] = [destination]

    for key in adj:
        adj[key].sort()

    return dfs_recursive('ICN', adj, ['ICN'], len(tickets))


def dfs_recursive(node, graph, visited, full_size):

    if len(visited)-1 == full_size:
        return visited

    if graph.get(node):
        for idx, next in enumerate(graph[node]):
            graph[node].pop(idx)
            visited.append(next)
            result = dfs_recursive(next, graph, visited, full_size)
            if result:
                return result
            else:
                graph[node].insert(idx, next)
                visited.pop()


'''
9/5 시도2
접근법
    각 항공권 티켓을 node로 생각하고 문제에 접근
    1) 출발지가 ICN인 티켓으로부터 시작하여 모든 티켓을 사용할때까지 DFS(DFS로 탐색하면 그 방문순서자체가 답이니)
    2) 단 DFS시, 결과를 알파벳순서가 앞서는 것으로 내어야하므로 알파벳 오름차순으로 티켓을 정렬한 후에 DFS를 수행
 
결과
    4개중 1개 틀림
    주석의 (1)과 (2)에 의해 약간 실수가 있었다.
    4개 테스트 케이스 중 1번이 오답
'''

def solution2(tickets):
    answer = ['ICN']

    tickets.sort(reverse=True)
    for idx in reversed(range(len(tickets))):  # (2) (1)을 위해 내림차순 정렬하였으므로 역순으로 탐색필요
        if tickets[idx][0] == 'ICN':
            start_idx = idx
            visited = []
            if dfs(start_idx, tickets, visited):
                break

    for idx in visited:
        answer.append(tickets[idx][1])
    return answer


def dfs(start_idx, tickets, visited):
    stack = [start_idx]

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)
            for idx in range(len(tickets)):
                if tickets[current][1] == tickets[idx][0]:  # (1) 주의-stack이므로 오름차순 정렬 시 알파벳 순서가 늦은녀석을 먼저 탐색
                    stack.append(idx)
    if len(visited) == len(tickets):
        return True
    return False
'''
9/5 시도1
접근법
    1. 각 공항마다 몇 번 가야 하는지 저장
    2. BFS돌면서 필요 횟수 만큼 각 공항을 경유
    3. 경유때마다 부모 Node를 기록..
    하지만... 이걸로는 풀리지가 않는다..
    
       
결과
    시간을 상당히 투자해도 해결할 수가 없다.
    각 공항을 여러번 경유할 수 있기 때문에 복잡도가 너무 높다.
    복잡도를 줄이기 위해 티켓 자체를 node로 생각하여 문제에 접근해보자
'''

def solution1(tickets):
    answer = []

    visit_capa = dict()
    adj = dict()

    # start point
    visit_capa['ICN'] = 1

    for ticket in tickets:
        start = ticket[0]
        destination = ticket[1]

        # calculating visit capacity
        if visit_capa.get(destination):
            visit_capa[destination] += 1
        else:
            visit_capa[destination] = 1

        # making adjacent list
        if adj.get(start):
            adj[start].append(destination)
        else:
            adj[start] = [destination]

    for key in adj:
        adj[key].sort()

    start = 'ICN'

    # BFS
    q = [start]

    parents = dict()
    parents[start] = [-1]
    visited = []

    while q:
        node = q.pop(0)
        if visit_capa[node] > 0:
            visit_capa[node] -= 1
            visited.append(node)

            if adj.get(node):
                for v in adj[node]:
                    q.append(v)
                    if parents.get(v):
                        parents[v].append(node)
                    else:
                        parents[v] = [node]

    return answer


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        # self.assertEqual(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]), ['ICN', 'JFK', 'HND', 'IAD'])
        self.assertEqual(solution([['ICN', 'SFO'],
                                   ['ICN', 'ATL'],
                                   ['SFO', 'ATL'],
                                   ['ATL', 'ICN'],
                                   ['ATL', 'SFO']]),
                         ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'])


if __name__ == '__main__':
    unittest.main()

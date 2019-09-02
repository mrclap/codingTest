import unittest

'''
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고,
컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.



제약조건 
    컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
    각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
    i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
    computer[i][i]는 항상 1입니다.

'''

'''
9/2 시도2
    식을 간단히 하여 다시 동일한 방법으로 풀었다.
    Pop을 사용하면 O(N)만큼 시간을 손해본다고 생각하였는데, 결론적으로
    다른분들이 pop을 이용하여 푼것보다 속도가 더 안나온다..
    
    왜 pop이 전혀 안느려지는걸까..
    
'''


def solution(n, computers):
    visited = {}
    q = [0]
    idx = 0
    count = 1
    flag = True
    while flag:  # O(N+E)
        if idx + 1 <= len(q):
            node = q[idx]
            if not visited.get(node):
                visited[node] = True
                for jdx in range(len(computers[node])):  # O(N)
                    if computers[node][jdx] == 1 and jdx != node:
                        q.append(jdx)
            else:
                idx += 1
        else:  # idx+1 > len(q)
            flag = False
            for idx in range(n):  # O(N)
                if not visited.get(idx):
                    q.append(idx)
                    count += 1
                    flag = True
                    break

    return count


def solution_with_pop(n, computers):  # bench mark
    def BFS(node, visit):
        que = [node]
        visit[node] = 1
        while que:  # O(N+E)
            v = que.pop(0)  # O(N)
            for i in range(n):  # O(N)
                if computers[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    que.append(i)
        return visit
    visit = [0 for i in range(n)]
    answer = 0
    for i in range(n):  # O(N)
        try:
            visit = BFS(visit.index(0), visit)
            answer += 1
        except:
            break
    return answer



'''
9/2 시도1
    1) 각 컴퓨터를 연결하고
    2) 연결된 컴퓨터들이 총 몇개의 set로 구성되었는지를 찾아야한다.
    3) BFS로 각 네트워크를 탐색하여, 최대로 연결하고, 그런 그룹이 몇 개가 나오는지 count해야 한다.
   
   list에서 pop을 통해 queue를 구현할 경우 연산속도가 많이 느려질 것으로 예상하여
   index를 이용해 queue를 구현하였다.
   
    
결과
    왜 이런 쉬운문제에 .. .12문제 중 4개나 틀리는 것일까..

'''


def solution1(n, computers):
    visited = {x: False for x in range(n)}
    q = [0]
    return bfs(n, computers, visited, q, q_idx=0, count=1)


def bfs(n, computers, visited, q, q_idx, count):
    if q_idx+1 > len(q):
        if len(q) == n:
            return count

        for idx in range(n):
            if not visited[idx]:
                visited[idx] = True
                q.append(idx)
                return bfs(n, computers, visited, q, q_idx+1, count+1)

    else:
        idx = q[q_idx]
        visited[idx] = True
        for jdx in range(len(computers[idx])):
            if computers[idx][jdx] == 1 and not visited[jdx] and jdx not in q:
                q.append(jdx)
        return bfs(n, computers, visited, q, q_idx + 1, count)


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        # self.assertEqual(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
        # self.assertEqual(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1)
        # self.assertEqual(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)
        # self.assertEqual(solution(3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 1)
        # self.assertEqual(solution(1, [[1]]), 1)

        # extreme case test
        import datetime

        N = 5000
        adj_matrix = []
        for idx in range(N):
            inner_list = list()
            for jdx in range(N):
                e = 1
                inner_list.append(e)
            adj_matrix.append(inner_list)

        start = datetime.datetime.now()
        print(start)
        self.assertEqual(solution_with_pop(N, adj_matrix), 1)
        print(datetime.datetime.now() - start)

        start = datetime.datetime.now()
        print(start)
        self.assertEqual(solution(N, adj_matrix), 1)
        print(datetime.datetime.now() - start)



if __name__ == '__main__':
    unittest.main()
    # numbers = [1, 1, 1, 1, 1]
    # target = 3
    #
    # print(solution(numbers, target))
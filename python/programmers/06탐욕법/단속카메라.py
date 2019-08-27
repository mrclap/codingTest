import unittest

'''
고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.
고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때,
모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

제약조건 
    차량의 대수는 1대 이상 10,000대 이하입니다.
    routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점,
    routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
    차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
    차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.
'''

'''
8/28 2차 시도
   다른 분들의 풀이를 바탕으로 더 직관적으로 코드를 수정 
   - > 정렬의 기준을 시작점이 아니라 끝점으로 !
 

'''


def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    last_camera = -30000

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer


'''
8/27 1차 시도
   1) 차량의 시작점을 기준으로 오름차순 정렬
   2) 차량의 시작점이 이전 차량들 중 가장 짧은 목적지보다 나중에 시작하기 직전까지의 시점을 찾음..
      해당 케이스 나타나면 카메라 하나 설치!
   3) 
   
결과
    효율성 5문제 중 1문제 실패
    sort에서 시간이 많이 걸리는 것으로 보임
    => [[0, 0], [0, 0], [2, 2]]), 2의 테스트 케이스를 만족하지 못하는 경우였다.
    if문의 조건을 수정하여 해결!
    
'''


def solution1(routes):
    answer = 0
    routes.sort(key=lambda x:x[0])
    out_min = routes[0][1]

    for each in routes[1:]:
        if each[0] > out_min: # if each[0] >= out_min:
            answer += 1
            out_min = each[1]
        else:
            if out_min > each[1]:
                out_min = each[1]
    answer += 1
    return answer


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([[0, 0], [0, 0], [2, 2]]), 2)
        self.assertEqual(solution([[0, 1], [0, 1], [2, 2]]), 2)
        self.assertEqual(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]), 2)


if __name__ == '__main__':
    unittest.main()




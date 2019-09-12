import unittest

'''
문제: https://www.welcomekakao.com/learn/courses/30/lessons/42889
다른사람풀이: https://www.welcomekakao.com/learn/courses/30/lessons/42889/solution_groups?language=python3
'''

'''
9/5 
    시작 09:43  
    종료 10:21
    11점 
    

'''


def solution(N, stages):
    people_in_stage = {stage: 0 for stage in range(1, N+2)}  # 1 ~ N+1
    people_clear_stage = {stage: 0 for stage in range(0, N+2)}  # 0 ~ N+1 (people_clear_stage[N+1] = 0)
    failure_stage = {stage: 0 for stage in range(1, N+1)}    # 1 ~ N

    for stage in stages:
        people_in_stage[stage] += 1

    people_clear_stage[N] = people_in_stage[N+1]

    for stage in reversed(range(1, N+1)):
        people_clear_stage[stage-1] = people_clear_stage[stage] + people_in_stage[stage]
        if people_clear_stage[stage-1] == 0:
            failure = 0
        else:
            failure = people_in_stage[stage] / people_clear_stage[stage-1]
        failure_stage[stage] = failure

    answer = list(failure_stage.keys())
    answer.sort(key=lambda x:failure_stage[x], reverse=True)
    return answer


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]), [3,4,2,1,5])
        self.assertEqual(solution(4, [4, 4, 4, 4, 4]), [4,1,2,3])


if __name__ == '__main__':
    unittest.main()

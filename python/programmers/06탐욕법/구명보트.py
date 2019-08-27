import unittest

'''
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.
예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만
1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.
사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제약조건 
    무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
    각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
    구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
    구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.
'''

'''
8/27 1차 시도
    무조건 2명 밖에 탈 수 없으므로 약간 문제가 간단해졌다.
    
    가장 가벼운 사람과 가장 무거운 사람을 항상 동시에 태우려고 노력하면 될까?
    -> Nope, When Limit= 100, [70, 50, 80, 50] 주어지면, 50-50을 쌍으로 태워야 한다. 
    
    그렇다면 가장 가벼운 두 명씩 태우면
    -> Nope, 다른 기회를 놓칠 수 있다. When Limit= 100, [30, 30, 70, 70] 주어지면, 30-70을 쌍으로 태워야 한다. 
    
    1) 오름차순 정렬 후,
    2) 첫번째 사람 선택 후(가장 가벼운) 가장 무거운 사람부터 차례로 탐색하여 합이 Limit이하인 경우를 찾아서 탑승시킨다.
    3) 두번째 사람 선택 후 직전에 탑승한 사람의 다음(이전)인덱스 부터 동일하게 검색하여 탑승 시킨다.
    4) 두 cursor(몸무게 가벼운사람부터 검색하는 녀석과 무거운사람부터 검색하는 녀석)이 만나거나, 
       가벼운사람부터 검색하는 커서의 값이 limit의 반을 초과하면 종료한다.
       
    생각보다 쉽게 문제가 풀렸다...
    

'''
def solution(people, limit):
    answer = 0
    min_weight_index_cursor = 0

    people.sort()
    for r_i in range(len(people)-1, -1, -1):
        # 두 명의 탑승이 가능하면
        if people[min_weight_index_cursor] + people[r_i] <= limit:
            min_weight_index_cursor += 1
        people.pop()
        answer += 1

        if min_weight_index_cursor >= r_i:
            break

    return answer


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([70, 50, 80, 50], 100), 3)
        self.assertEqual(solution([70, 50, 80], 100), 3)



if __name__ == '__main__':
    unittest.main()
    # print(solution("1924", 2))
    # print(solution("1231234", 3))
    # print(solution("111133255", 2))




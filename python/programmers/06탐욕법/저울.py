import unittest

'''
하나의 양팔 저울을 이용하여 물건의 무게를 측정하려고 합니다.
이 저울의 양팔의 끝에는 물건이나 추를 올려놓는 접시가 달려 있고, 양팔의 길이는 같습니다.
또한, 저울의 한쪽에는 저울추들만 놓을 수 있고, 다른 쪽에는 무게를 측정하려는 물건만 올려놓을 수 있습니다.


저울추가 담긴 배열 weight가 매개변수로 주어질 때,
이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값을 return 하도록 solution 함수를 작성해주세요.

예를 들어, 무게가 각각 [3, 1, 6, 2, 7, 30, 1]인 7개의 저울추를 주어졌을 때,
이 추들로 측정할 수 없는 양의 정수 무게 중 최솟값은 21입니다.



제약조건 
    저울추의 개수는 1개 이상 10,000개 이하입니다.
    각 추의 무게는 1 이상 1,000,000 이하입니다.
'''

'''
8/28 시도3
    recursive를 사용하다보니.. 21개의 추로 구성 된 문제를 푸는데에 7초가 넘게 걸린다.
    recursive를 줄이거나 사용하지 않는 법으로 가야하는데 ..
    심지어 제약조건이 추가 10,000개 이하이다...
    
    풀이를 cheating하였다...
    

'''
def benchmark_solution(weight):
    weight.sort()
    ans = 1
    for e in weight:
        if ans < e:
            break
        ans += e

    return ans


def solution(weight):
    weight.sort()

    if weight[0] != 1:
        return 1

    sum = []
    tmp_sum = 0

    for idx in range(len(weight)):
        tmp_sum += weight[idx]
        sum.append(tmp_sum)
        if idx < len(weight)-1 and tmp_sum+1 < weight[idx+1]:
            return tmp_sum+1
    return sum[-1]+1

    # https://ydeer.tistory.com/55



'''
8/28 시도2
    이번에는 weight를 정렬 후 재귀를 통해 추를 하나씩 뺴도록 해보았음.
    
    결과
        - 테스트1 빼고 모두 시간 초과

'''


def solution2(weight):
    answer = 0
    weight.sort()

    compare = 1

    while True:
        if not subtract_recursive2(compare, weight):
            return compare
        compare += 1
    return answer


def subtract_recursive2(left, weight):
    _weight = weight.copy()
    _left = left

    for idx in range(len(weight)-1, -1, -1):
        if _weight[idx] > _left:
            _weight.pop(idx)
        elif _weight[idx] <= _left:
            _left = _left - _weight[idx]
            _weight.pop(idx)
            if _left == 0:
                return True
            subtract_recursive(_left, _weight)

    return False

'''
8/28 무식하게 풀어보자.
    1. 재귀로 모든 경우의 추의 조합을 도출해내고
    2. 추들의 합을 계산한다.
    3. 중복을 없애고 sort하여 오름차순 정렬 후
    4. 값을 1부터 1씩 증가시키며 없는 수를 찾아낸다.
    
    상당히 비효율적이라는 생각이 드는데..
    역시나 모든 case에 시간초과 ....
    
'''


def solution1(weight):
    answer = 0
    combination_list = []
    recursive([], weight, combination_list)

    sum_of_combination_list = [sum(x) for x in combination_list]
    sum_set = set(sum_of_combination_list)

    compare = 1
    for each in sum_set:
        if each != compare:
            return compare
        compare += 1

    return answer


def recursive(combination, unused_weight, combination_list):
    for idx in range(len(unused_weight)):

        _combination = combination.copy()
        _combination.append(unused_weight[idx])
        combination_list.append(_combination)

        _unused_weight = unused_weight.copy()
        _unused_weight.pop(idx)

        recursive(_combination, _unused_weight, combination_list)


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([3, 1, 6, 2, 7, 30, 1]), 21)
        self.assertEqual(solution([1, 1, 1]), 4)
        self.assertEqual(solution([1, 2, 3]), 7)
        self.assertEqual(solution([1, 10]), 2)
        self.assertEqual(solution([1, 1, 3]), 6)
        # self.assertEqual(solution([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), 22)


if __name__ == '__main__':
    unittest.main()




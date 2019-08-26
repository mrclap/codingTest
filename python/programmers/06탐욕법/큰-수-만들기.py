import unittest

'''
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제약조건 
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.
'''

'''
8/26 cheating
    programmers에서 문제를 푼 다른분들의 답을 보니, 미리 list에 숫자를 모두 넣는것이 아니라.
    stack방식으로 하나씩 숫자를 추가하고, 조건에따라 검증하여 삭제하는 방식을 취했다...
    이게 자료구조의 힘이구나 .. 난 공부가 많이 필요하다...
'''


def solution(number, k):
    number_stack = []

    for num in number:
        while number_stack and number_stack[-1] < num and k > 0:
            number_stack.pop()
            k -= 1
        number_stack.append(num)
    return ''.join(number_stack[:len(number)-k])


'''
8/21 5차 시도

결과
    - 정답률 : 7/12
    - 엉망..2
    - '-1'이 2개 이상 연속으로 있는 경우에 대한 처리를 하였으나,,, 8,10번 포함 더 틀림...
    what.. the ...

'''




ELIMINATED = -1


def solution5(number, k):
    answer = ''
    number_list = [int(each) for each in number]

    idx = 0
    idx_offset = 1
    count = 0
    while True:
        # 마지막까지 가면
        if idx == (len(number_list) - count - 1):
            number_list[idx] = ELIMINATED
            count += 1
            idx -= 1
        # 이미 삭제된 자리이면
        elif number_list[idx] == ELIMINATED:
            idx += 1
        # 조건을 만족하면
        else:
            if number_list[idx+1] == ELIMINATED:
                while number_list[idx+idx_offset] == ELIMINATED:
                    idx_offset += 1

            if number_list[idx] < number_list[idx+idx_offset]:
                number_list[idx] = ELIMINATED
                count += 1
                idx = 0
            else:
                idx += 1

            idx_offset = 1

        if k == count:
            # -1 제외한 숫자를 str으로 변환
            for number in number_list:
                if number != ELIMINATED:
                    answer += str(number)

            return answer

    return 'error'

'''
8/21 4차 시도

결과
    - 정답률 : 3/12
    - 엉망..
    - 삭제될 수에 '-1'을 대입하는 방식으로 진행하였으나 ... 결과가 엉망이다.
    -> '-1'이 2개 이상 연속으로 있는 경우에 대한 처리가 필요했다.


'''

ELIMINATED = -1


def solution4(number, k):
    answer = ''
    number_list = [int(each) for each in number]

    idx = 0
    idx_offset = 1
    count = 0
    while True:
        # 마지막까지 가면
        if idx == (len(number_list) - count - 1):
            number_list[idx] = ELIMINATED
            count += 1
            idx -= 1
        # 이미 삭제된 자리이면
        elif number_list[idx] == ELIMINATED:
            idx += 1
        # 조건을 만족하면
        else:
            if number_list[idx+1] == ELIMINATED:
                idx_offset += 1

            if number_list[idx] < number_list[idx+idx_offset]:
                number_list[idx] = ELIMINATED
                count += 1
                idx = 0
            else:
                idx += 1

            idx_offset = 1

        if k == count:
            # -1 제외한 숫자를 str으로 변환
            for number in number_list:
                if number != ELIMINATED:
                    answer += str(number)

            return answer

    return 'error'

'''
8/20 3차 시도
    
결과
    - 정답률 : 7/12
    - 5번 ~ 10번 시간초과
    - hashmap을 이용해서 pop이후 list를 재배치하는 연산을 줄이려고 했는데
    오히려 시간이 더 걸린다.
    
    
'''


def solution3(number, k):
    number_list = {idx: number[int(idx)] for idx in range(len(number))}

    idx = 0
    # print(list(number_list.keys()))

    while True:
        number_list_keys = list(number_list.keys())
        hash_key = number_list_keys[idx]
        if hash_key == number_list_keys[-1]:
            del number_list[hash_key]
            k -= 1
            idx = 0
        elif number_list[hash_key] < number_list[number_list_keys[idx+1]]:
            del number_list[hash_key]
            k -= 1
            idx = 0
        else:
            idx += 1

        if k == 0:
            return ''.join(list(number_list.values()))

    return 'error'


'''
8/20 2차 시도
    치명적인 실수, 해당 idx가 마지막 idx인지 확인할때는 값이 같은지 확인하는게 아니다!!
    
결과
    - 정답률 : 10/12
    - 8번 10번 시간초과
    - if k == 0인 조건을 성립하지 못하는 케이스가 있는지 살펴보자.
'''


def solution2(number, k):
    number_list = [each for each in number]

    idx = 0
    while True:
        if idx == len(number_list)-1:
            number_list.pop(idx)
            k -= 1
            idx = 0
        elif number_list[idx] < number_list[idx+1]:
            number_list.pop(idx)
            k -= 1
            idx = 0
        else:
            idx += 1
        if k == 0:
            return ''.join(number_list)

    return 'error'


'''
8/20 1차시도

test case
    - 943254, 1 => 2(idx:3)삭제
    - 38565, 3 => 3(0), 5(2), 5(4) 삭제
    - 9124, 2 => 1(1), 4(3) 삭제
    - 1434928, 2 => 1(0), 3(2) 삭제
    -> 가장 왼쪽부터 쭉 훑으면서 1)왼쪽의 수가 2)그 바로 다음 수보다 작으면 삭제, 없으면 마지막 삭제
    
결과
    - 정답률 : 7/12
    
'''


def solution1(number, k):
    number_list = [each for each in number]

    idx = 0
    while True:
        if number_list[idx] == number_list[-1] or number_list[idx] < number_list[idx+1]:
            number_list.pop(idx)
            k -= 1
            idx = 0
        else:
            idx += 1

        if k == 0:
            return ''.join(number_list)

    return 'error'


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution("1924", 2), "94")
        self.assertEqual(solution("1231234", 3), "3234")
        self.assertEqual(solution("4177252841", 4), "775841")
        # 추가
        self.assertEqual(solution("333311", 2), "3333")
        self.assertEqual(solution("111133255", 2), "1133255")

        # 추가2
        self.assertEqual(solution("11111133255", 3), "11133255")

        # extreme test case
        # long_str = "".join(["1" for e in range(1_000_000)])
        # long_str_answer = "".join(["1" for e in range(999_999, 1_000_000)])
        # self.assertEqual(solution(long_str, 999_999), long_str_answer)
        #
        # long_str = "".join(["9" for e in range(1_000_000)])
        # long_str_answer = "".join(["9" for e in range(999_999, 1_000_000)])
        # self.assertEqual(solution(long_str, 999_999), long_str_answer)


if __name__ == '__main__':
    unittest.main()
    # print(solution("1924", 2))
    # print(solution("1231234", 3))
    # print(solution("111133255", 2))




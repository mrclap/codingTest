import unittest

'''
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록
solution 함수를 작성해주세요.



제약조건 
    주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
    각 숫자는 1 이상 50 이하인 자연수입니다.
    타겟 넘버는 1 이상 1000 이하인 자연수입니다.
'''

'''
9/2 시도1
    후위연산으로 재귀를 이용해 모든 경우의 수에 대한 연산식을 만들어서 풀었다.
    굳이 후위연산식을 가져가지말고 그냥 계산해도 아무 문제는 없을듯


'''
PLUS = '+'
MINUS = '-'


def solution(numbers, target):
    answer = 0
    operations_list = []
    numbers = [0] + numbers
    recursive(len(numbers), [], operations_list)
    for operation in operations_list:
        if target == computer([numbers, operation]):
            answer += 1

    return answer


def computer(row_equation):
    numbers, operations = row_equation
    computing = numbers[0]
    for idx in range(len(operations)):
        if operations[idx] == PLUS:
            computing += numbers[idx + 1]
        elif operations[idx] == MINUS:
            computing -= numbers[idx + 1]

    return computing


def recursive(count, operations, operations_list):
    count -= 1
    if count > 0:
        recursive(count, operations + [PLUS], operations_list)
        recursive(count, operations + [MINUS], operations_list)
    else:
        operations_list.append(operations)


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([1, 1, 1, 1, 1], 3), 5)
        # self.assertEqual(solution([1, 1, 1, 1, 1], 3), 5)


if __name__ == '__main__':
    unittest.main()
    # numbers = [1, 1, 1, 1, 1]
    # target = 3
    #
    # print(solution(numbers, target))
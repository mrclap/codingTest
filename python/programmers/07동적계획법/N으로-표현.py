import unittest

'''
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.



제약조건 
    N은 1 이상 9 이하입니다.
    number는 1 이상 32,000 이하입니다.
    수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
    최솟값이 8보다 크면 -1을 return 합니다.
'''

'''
8/30 1차 시도
   모..든 경우에 대해서 N을 조합해가며 답을 찾아야 할 것 같다.
   N = 5 / number = 12 라면
   
   1) N 1개 사용시
    12 = 5
   
   2) N 2개 사용시
    12 = 5+5
    12 = 5-5 ( <-- 시작하지 않아도 될 듯)
    12 = 5*5
    12 = 5/5 ( <-- 1 )
    12 = 55
    
   3) N 3개 사용시
    12 = (5+5)+5
    12 = (5+5)-5
    12 = (5+5)*5
    12 = (5+5)/5
    12 = (5+55)
    
    12 = (5-5)+5
    12 = (5-5)-5
    12 = (5-5)*5
    12 = (5-5)/5
    12 = (5-55)
    .
    .
    
    와 같은 방식으로 반복한다..
    다만 위에서 보이듯.. NN의 형태.. 즉 55를 만드는 과정이 약간 지저분해 보이는데 ...
    
    결과
        10개 중 2개 오답..
        정말 거대하고 지저분한 코드가 탄생했다.
        
   

'''
import copy

PLUS = '+'
MINUS = '-'
MULTIPLY = '*'
DIVIDE = '/'


def solution(N, number):
    answer = 0

    if number == N:
        return 1

    N_plus_N = [[N, N], [PLUS]]
    N_multiply_N = [[N, N], [MULTIPLY]]
    N_divide_N = [[N, N], [DIVIDE]]
    NN = [[N * 10 + N], []]

    if answer in (computer(N_plus_N), computer(N_multiply_N), computer(N_divide_N), computer(NN)):
        return 2

    # Do recursive
    count_list = []
    for each in [N_plus_N, N_multiply_N, N_divide_N, NN]:
        solver(N, number, each, count=2, count_list=count_list)

    if count_list:
        answer = min(count_list)
    else:
        answer = -1

    return answer


def computer(row_equation):
    numbers, operations = row_equation
    computing = numbers[0]
    for idx in range(len(operations)):
        if operations[idx] == PLUS:
            computing += numbers[idx + 1]
        elif operations[idx] == MINUS:
            computing -= numbers[idx + 1]
        elif operations[idx] == MULTIPLY:
            computing *= numbers[idx + 1]
        elif operations[idx] == DIVIDE:
            computing //= numbers[idx + 1]
        if computing == 0:
            return 0

    return computing


def solver(N, number, row_equation, count, count_list):
    if computer(row_equation) != 0:
        count += 1
        if count >= 9:
            return

        # 더하기
        row_equation_plus = copy.deepcopy(row_equation)
        row_equation_plus[0].append(N)
        row_equation_plus[1].append(PLUS)
        if number == computer(row_equation_plus):
            count_list.append(count)

        # 빼기
        row_equation_minus = copy.deepcopy(row_equation)
        row_equation_minus[0].append(N)
        row_equation_minus[1].append(MINUS)
        if number == computer(row_equation_minus):
            count_list.append(count)

        # 곱하기
        row_equation_multiply = copy.deepcopy(row_equation)
        row_equation_multiply[0].append(N)
        row_equation_multiply[1].append(MULTIPLY)
        if number == computer(row_equation_multiply):
            count_list.append(count)

        # 나누기
        row_equation_divide = copy.deepcopy(row_equation)
        row_equation_divide[0].append(N)
        row_equation_divide[1].append(DIVIDE)
        if number == computer(row_equation_divide):
            count_list.append(count)

        # 숫자 하나 더하기
        row_equation_NN = copy.deepcopy(row_equation)
        n = row_equation_NN[0].pop()
        row_equation_NN[0].append(n*10+N)
        if number == computer(row_equation_NN):
            count_list.append(count)

        for each in [row_equation_plus, row_equation_minus, row_equation_multiply, row_equation_divide, row_equation_NN]:
            solver(N, number, each, count, count_list)


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(5, 12), 4)
        self.assertEqual(solution(2, 11), 3)
        self.assertEqual(solution(5, 3600), 8)


if __name__ == '__main__':
    unittest.main()




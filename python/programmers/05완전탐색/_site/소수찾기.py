'''
문제 설명

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.
제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
입출력 예
numbers	return
17	3
011	2
입출력 예 설명
예제 #1
[1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.
예제 #2
[0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
11과 011은 같은 숫자로 취급합니다.
'''

'''
5/26 1차 시도 pass

- 집중이 안되서 오래걸렸다.
- itertool이라는 라이브러리가 있는줄 몰랐다..
- isPrime함수가 무언가 깔끔하지 못한 느낌이든다..

'''
import math


def solution(numbers):
    numbers = [x for x in numbers]
    results = []
    answer = 0

    for each in numbers:
        if each != '0':
            _numbers = numbers.copy()
            str = each
            _numbers.remove(each)
            results.append(str)
            recursive(str, _numbers, results)

    results = set([int(x) for x in results])

    for result in results:
        if is_prime(result):
            answer += 1

    return answer


def recursive(previous, numbers, results):
    for each in numbers:
        _numbers = numbers.copy()
        current = previous + each
        _numbers.remove(each)
        results.append(current)
        recursive(current, _numbers, results)


def is_prime(n):
    if n <= 1:
        return False

    START = 2
    # 1. 2~ floor(root(n)) => z 까지 범위의 list or dict 생성
    # 2. for loop으로 1. 숫자를 순회하면서
    # 3. 해당 loop의 수(d)가 n을 나눌 수 있는지 ( % d == 0)판별
    # 4. 나눠지지 않으면 해당 수의 배수 중 z보다 작은 수를 모두 소거
    candidates_dict = {x: 1 for x in range(START, math.floor(math.sqrt(n))+1)}
    for x in candidates_dict:
        if candidates_dict[x] == 1:
            if n % x != 0:
                candidates_dict[x] = 0
            set_0_for_all_multiples(x, candidates_dict)
    prime_numbers = []

    for x in candidates_dict:
        if candidates_dict[x] == 1:
            prime_numbers.append(x)

    result = True if len(prime_numbers) == 0 else False
    return result


def set_0_for_all_multiples(n, dict):
    for x in range(n*2, len(dict)+2, n):
        if dict[x] == 1:
            dict[x] = 0


if __name__ == '__main__':
    numbers = "17"      # "3"
    # numbers = "011"   # "2"
    print(solution(numbers))
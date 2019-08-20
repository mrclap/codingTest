from datetime import datetime

'''
문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.

'''
import unittest
'''
7/26 2차 시도

- 도무지 방법이 떠오르지 않아 '질문하기'를 cheating했다.
- 나는 계속해서 'A'를 피하는 방법에 대해 고민했는데 오히려 'A'가 아닌 알파벳을 찾아가는 방식으로 접근해야 쉽게 풀이가 가능해보인다.

'''

def solution(name):
    answer = 0
    name_list = [each for each in name]

    # 조이스틱 상하 이동 계산
    for each in name_list:
        answer += min(ord(each)-ord('A'), ord('Z')+1-ord(each))

    left_right_steps = []

    def dfs(cursor_idx, name_list, current_steps):
        is_over = True
        for each in name_list:
            if each != 'A':
                is_over = False
        if is_over:
            return left_right_steps.append(current_steps)

        is_entered = False
        for idx in range(len(name_list)):
            if name_list[cursor_idx + idx] != 'A':
                new_name_list = name_list
                new_name_list[cursor_idx + idx] = 'A'
                dfs(cursor_idx=cursor_idx + idx, name_list=new_name_list, current_steps=current_steps + idx )
                is_entered = True
            if name_list[cursor_idx - idx] != 'A':
                new_name_list = name_list
                new_name_list[cursor_idx - idx] = 'A'
                dfs(cursor_idx=cursor_idx - idx, name_list=new_name_list, current_steps=current_steps + idx)
                is_entered = True

            if is_entered:
                return
    dfs(0, name_list, 0)

    answer += min(left_right_steps)
    return answer



'''
7/25 1차 시도

1. 각 글자의 'A'로 부터의 거리
    -> 'A' - 각 글자 / 각 글자 - 'Z' + 1 중 작은 수 선택 ( A = 65, 91 ) 
2. 가장 많이 A가 연속되는 곳 바로 앞에서 A의 갯수와 처음부터의 거리 중 작은 것 선택해서 더 하기
3. 그리고 부족한 로직에 덧붙는 지저분한 .. 조건들 .......... 

채점 결과
정확성: 45.5
합계: 45.5 / 100.0

>> 너무 지저분한 코드와 로직... 반성하자.. 심지어 틀렸다.

'''
def solution1(name):
    answer = 0
    name_list = [each for each in name]
    for each in name_list:
        answer += min(ord(each)-ord('A'), ord('Z')+1-ord(each))

    start_index_of_max = -1
    end_index_of_max = -1
    index = -1
    counter = 0
    max = 0
    for idx in range(len(name_list)):
        if name_list[idx] == 'A':
            if idx != 0 and name_list[idx-1] == 'A':
                counter += 1
            else:
                index = idx
                counter = 1
        if max < counter:
            max = counter
            start_index_of_max = index
            end_index_of_max = index + counter

    answer += len(name) - 1
    if start_index_of_max == -1:
        print("no A in name")
        pass
    elif start_index_of_max < max+1:  # 가장 긴 연속된 A의 앞에서 되돌아 진행할때
        answer += (start_index_of_max-1)*2 - end_index_of_max + 1
        print(max, start_index_of_max, end_index_of_max, "reverse")
    else:  #  그냥 순서대로 진행할때
        print("go Strait")
        if index+counter == len(name):
            answer -= counter
            print(index, counter, "go Strait and end with A")
    return answer


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution('JEROEN'), 56)
        self.assertEqual(solution('JAN'), 23)


if __name__ == '__main__':
    # unittest.main()
    print(solution('JEROEN'))
    print(solution('JAN'))
    print(solution('AAAAAAAAAAAA'))
    print(solution('JAAAAAAAAJAAAAAAM'))







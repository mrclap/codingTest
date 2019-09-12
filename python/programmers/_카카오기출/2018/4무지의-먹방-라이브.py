import unittest

'''
문제: https://www.welcomekakao.com/learn/courses/30/lessons/42890#
다른사람풀이: https://www.welcomekakao.com/learn/courses/30/lessons/42890/solution_groups?language=python3
'''

'''
9/5 
    시작 10:23  
    종료 12:36 
    
    못품... 미쳤다.. 2시간 낭비
    
    마감 14:00
    0점 
    

'''


def solution(relation):
    candidate_keys = []

    row_size = len(relation)
    col_size = len(relation[0])

    def checker(key_set):
        if len(key_set) == 0:
            return False

        key_idxs = list(key_set)
        for ref in range(row_size):
            key = set()
            for key_idx in key_idxs:
                key.add(relation[ref][key_idx])
            counter = 0
            for compare in range(row_size):
                # print(key, set(relation[compare]))
                # print(key.issubset(set(relation[compare])))
                if key.issubset(set(relation[compare])):
                    counter += 1
                if counter >= 2:
                    return False
        return True


    def recursive(key_set, left):
        is_minimal = True
        for candidate_key in candidate_keys:
            if candidate_key.issubset(key_set):
                is_minimal = False

        if is_minimal and checker(key_set):
            candidate_keys.append(key_set.copy())

        else:
            for idx, new_key in enumerate(left):
                if {new_key}.issubset(key_set):
                    continue
                left.pop(idx)
                key_set.add(new_key)

                recursive(key_set, left)
                key_set.pop()
                left.insert(idx, new_key)
    recursive(set(), [x for x in range(col_size)])
    answer = len(candidate_keys)
    return answer



# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]),
                         2)

if __name__ == '__main__':
    unittest.main()

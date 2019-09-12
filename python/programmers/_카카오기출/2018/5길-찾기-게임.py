import unittest

'''
문제: https://www.welcomekakao.com/learn/courses/30/lessons/42891
다른사람풀이: https://www.welcomekakao.com/learn/courses/30/lessons/42891/solution_groups?language=python3
'''

'''
9/5 
    시작 12:37  
    종료 13:02 - 비효율코드
    
    
        마감 14:00
    0점 
    

'''


def solution(food_times, k):
    food_times_dic = {}
    for idx, time in enumerate(food_times):
        food_times_dic[idx] = time

    sorted_keys = list(food_times_dic.keys())
    sorted_keys.sort(key=lambda x: food_times_dic[x])
    dish_size = len(food_times)
    cursor = 0
    loop = 0

    for idx, key in enumerate(sorted_keys):
        offset = 0
        for jdx in range(idx):
            if key > sorted_keys[jdx]:
                offset -= 1
            if idx >= 1:
                if sorted_keys[idx-1] < key:
                    loop -= 1
        required_sec = (food_times_dic[key] - 1 - loop) * dish_size + key + offset - cursor + 1
        if required_sec < k:
            k = k - required_sec
            loop += (food_times_dic[key] - loop)
            dish_size -= 1
        else:
            left = (k + cursor) % dish_size
            shifter = 0
            for jdx in range(idx):
                if sorted_keys[jdx] < left:
                    shifter += 1
            return (left + shifter) % dish_size + 1

        cursor = key + offset - cursor

# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution([3,1,2], 5), 1)

if __name__ == '__main__':
    unittest.main()

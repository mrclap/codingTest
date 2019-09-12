import unittest

'''
문제: https://www.welcomekakao.com/learn/courses/30/lessons/42888?language=python3
다른사람풀이: https://www.welcomekakao.com/learn/courses/30/lessons/42888/solution_groups?language=python3
'''

'''
9/5 
    시작 09:06  
    종료 09:41
    9점
    

'''
ENTER = 'Enter'
LEAVE = 'Leave'
CHANGE = 'Change'

SENTENCE_IN = '님이 들어왔습니다.'
SENTENCE_OUT = '님이 나갔습니다.'


def solution(record):
    answer = []

    nicknames = {}
    action_and_id_list = []

    for each in record:
        action = each.split(' ')[0]
        if action == LEAVE:
            [_, user_id] = each.split(' ')
            action_and_id_list.append([action, user_id])
        else:
            [_, user_id, nickname] = each.split(' ')
            # ['Enter' , 'uid1234', 'Muzi']
            if action == ENTER:
                nicknames[user_id] = nickname
                action_and_id_list.append([action, user_id])
            else:  # action == CHANGE
                nicknames[user_id] = nickname

    for action_and_id in action_and_id_list:
        [action, user_id] = action_and_id
        nickname = nicknames[user_id]
        if action == ENTER:
            answer.extend([nickname+SENTENCE_IN])
        else:
            answer.extend([nickname+SENTENCE_OUT])

    return answer


# test Module
class TestMethods(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(["Enter uid1234 Muzi",
                                    "Enter uid4567 Prodo",
                                    "Leave uid1234",
                                    "Enter uid1234 Prodo",
                                    "Change uid4567 Ryan"]),
                                 ["Prodo님이 들어왔습니다.",
                                  "Ryan님이 들어왔습니다.",
                                  "Prodo님이 나갔습니다.",
                                  "Prodo님이 들어왔습니다."])


if __name__ == '__main__':
    unittest.main()

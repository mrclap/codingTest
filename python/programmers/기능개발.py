# -*- coding: utf-8 -*-

def solution(progresses, speeds):
    answer = []

    return answer

'''
first trial
90/100

def solution(progresses, speeds):
    answer = []
    progresses_left = [100 - each for each in progresses]
    days_to_finish = list()
    for i in range(len(progresses_left)):
        days_to_finish.append(progresses_left[i] / speeds[i])

    for idx in range(len(days_to_finish)):
        if days_to_finish[idx] == 0:
            days_to_finish[idx] = 1

    counter = 0

    for idx, each in enumerate(days_to_finish):
        bottle_neck = days_to_finish[sum(answer)]  # 가장 우선 처리되어야 하는 작업의 작업 잔여일
        if each is bottle_neck:  # 내 자신이면 counter + 1 하고 다음!
            counter += 1
        elif each <= bottle_neck:  # 현재 우선 처리되어야 하는 작업과 동시에 배포가 가능하면
            counter += 1
        else:  # 뒤의 잔여 작업이 더 늦게 끝나면 현재 배포가능한 것까지 배포
            answer.append(counter)  # 배포한 수 만큼 answer에 넣고
            counter = 1  # 카운터 0로 초기화 하고

        if idx == len(days_to_finish) - 1:  # 현재 작업이 마지막 작업이라면
            if counter != 0:
                answer.append(counter)
            else:
                answer.append(1)

    return answer
'''

if __name__ == '__main__':
    progresses = [99, 90, 92]
    speeds = [100, 1, 1]
    print(solution(progresses, speeds))

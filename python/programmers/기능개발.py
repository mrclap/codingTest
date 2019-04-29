# -*- coding: utf-8 -*-
'''
bench mark solution
'''
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]



'''
Second trial
100/100

pop으로 list의 값을 하나씩 지우면서 While문 돌


def solution(progresses, speeds):
    answer = []
    progresses_left = [100 - each for each in progresses]
    days_to_finish = list()

    # 7.02 days - > 8 days
    for i in range(len(progresses_left)):
        left_days = progresses_left[i] / speeds[i]
        if left_days % 1 != 0:
            left_days = int(left_days) + 1
        else:
            left_days = int(left_days)
        days_to_finish.append(left_days)

    reference_days = 0
    counter = 0

    while days_to_finish:
        current = days_to_finish.pop(0)

        # 현재의 작업이 처음이면
        if reference_days == 0:
            reference_days = current
            counter += 1

        # 만약 현재의 작업이 버틀넥보다 먼저 혹은 동시에 끝난다면
        # counter 올려줌
        elif current <= reference_days:
            counter += 1

        # 만약 현재의 작업이 버틀넥보다 더 걸리면
        else:
            # 바로 앞의 작업까지의 counter를 answer에 넣고
            answer.append(counter)

            # 기준 값 바꾸고
            reference_days = current

            # counter 초기화 하고
            counter = 1

        # 현재 작업이 마지막 작업이면 counter 하나 올리고 answer에 넣어주고 끝
        if len(days_to_finish) == 0:
            answer.append(counter)

    return answer
'''


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
    # progresses = [99, 90, 92]
    # speeds = [100, 1, 1]
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))

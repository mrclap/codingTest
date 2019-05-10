import heapq, math
'''
3차 시도
5/9 성공
[2] 작업 도중에 대기 작업이 없어서 대기하는 경우 처리

코드는 조금 더 깔끔하게 직관적으로 수정해야 할 듯
'''

def solution(jobs):
    answer = 0
    candidates = []
    total_length = len(jobs)

    # jobs을 작업이 들어온 순서대로 정렬
    jobs.sort(key=lambda x: x[0])

    # 가장 먼저 처리해야하는 작업의 요청시간이 0이 아닐 수 있으므로
    current = jobs[0][0]        # <---- [1]

    # 이미 들어온 작업을 candidates에 넣음
    start = 0

    while True:
        for idx in range(start, len(jobs)):
            if jobs[idx][0] <= current:  # 현재 처리 가능한 작업이면
                heapq.heappush(candidates, (jobs[idx][1], jobs[idx][0]))
                start = idx + 1
            else:  # [자주하는 실수!!!}
                # 조건을 만족하지 못했을때 더 이상 loop을 돌지 않도록 break 해줄 것!
                # 이미 오름차순 정렬 되어있으므로!
                break

        if len(candidates) != 0:
            next_job = heapq.heappop(candidates)
            answer = answer + (current - next_job[1]) + next_job[0]
            current = current + next_job[0]  # 현재 시간에 작업시간 더 해주고
            if len(jobs) == start and not candidates:
                break
        else:
            current = jobs[start][0]    # <---- [2] 작업 도중에 대기 작업이 없어서 대기하는 경우 처리

    answer = math.floor(answer / total_length)

    return answer


'''
2차 시도
5/9 런타임에러 5%
[1] 초기작업이 바로 시작되지 않는 경우(요청시간이 0인 작업이 없는 경우) 처리


def solution(jobs):
    answer = 0
    candidates = []
    total_length = len(jobs)

    # jobs을 작업이 들어온 순서대로 정렬
    jobs.sort(key=lambda x: x[0])

    # 가장 먼저 처리해야하는 작업의 요청시간이 0이 아닐 수 있으므로
    current = jobs[0][0]        # <---- [1]

    # 이미 들어온 작업을 candidates에 넣음
    start = 0

    while True:
        for idx in range(start, len(jobs)):
            if jobs[idx][0] <= current:  # 현재 처리 가능한 작업이면
                heapq.heappush(candidates, (jobs[idx][1], jobs[idx][0]))
                start = idx + 1
            else:  # [자주하는 실수!!!}
                # 조건을 만족하지 못했을때 더 이상 loop을 돌지 않도록 break 해줄 것!
                # 이미 오름차순 정렬 되어있으므로!
                break
        next_job = heapq.heappop(candidates)
        answer = answer + (current - next_job[1]) + next_job[0]
        current = current + next_job[0]  # 현재 시간에 작업시간 더 해주고
        if len(jobs) == start and not candidates:
            break
    if answer != 0:
        answer = math.floor(answer / total_length)

    return answer
'''

'''
5/9 런타임에러 70%

def solution(jobs):
    answer = 0
    current = 0     # 현재시각
    candidates = []
    total_length = len(jobs)

    # jobs을 작업이 들어온 순서대로 정렬
    jobs.sort(key=lambda x: x[0])

    # 이미 들어온 작업을 candidates에 넣음
    start = 0
    while True:
        for idx in range(start, len(jobs)):
            if jobs[idx][0] <= current:  # 현재 처리 가능한 작업이면
                heapq.heappush(candidates, (jobs[idx][1], jobs[idx][0]))
                start = idx + 1
            else:   # [자주하는 실수!!!}
                    # 조건을 만족하지 못했을때 더 이상 loop을 돌지 않도록 break 해줄 것!
                    # 이미 오름차순 정렬 되어있으므로!
                break
        next_job = heapq.heappop(candidates)
        answer = answer + (current - next_job[1]) + next_job[0]
        current = current + next_job[0]  # 현재 시간에 작업시간 더 해주고
        if len(jobs) == start and not candidates:
            break

    answer = math.floor(answer / total_length)

    return answer
'''

if __name__ == '__main__':
    # jobs = [[0, 3], [2, 6], [1, 9]]
    jobs = [[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]
    print(solution(jobs))

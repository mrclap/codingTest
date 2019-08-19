from datetime import datetime

'''
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다.
다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
학생들의 번호는 체격 순으로 매겨져 있어,
바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
체육복이 없으면 수업을 들을 수 없기 때문에
체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n,
체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
'''

'''
6/25 코드 개선 / 밴치마크 코드(programmers)

코드가 마음에 들지 않아 아예 처음부터 다시 짜보았다.
비록 코드가 조금 길어지기는 하지만,
lost와 reserve의 중복을 제거하는 로직에서 for문의 중복을 피하기 위해 dictionary(->list)를 사용했다.

1) 작성 후, 다른 분께서 
`[r for r in reserve if r not in lost]의 이중for문을 통해 아주 간결하게 짜놓은 코드와 성능비교를 했는데...`
내 코드가 30배 가량 *느렸다...*

2) 조건을 조금 극단적으로 주었더니 
    n = 10001 
    lost = [i for i in range(10000, 1, -1) if i % 2 == 1],
    reserve = [i for i in range(10000, 1, -1) if i % 2 == 0]
list의 성능이 월등히 좋아졌다.
    

'''

def solution_benchmark(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)


def solution(n, lost, reserve):
    # lost.sort()
    # reserve.sort()

    answer = n - len(lost)

    '''
    LOGIC
    1) lost와 reserve에 모두 존재하는 학생 제거
    2) lost학생의 앞뒤 체크
        2.1) index: 1 -> 뒤만 체크
        2.2) index: n -> 앞만 체크
    '''

    # 1) lost와 reserve에 모두 존재하는 학생 제거
        # loop 효율을 위해 dictionary사용
    lost_dict = [False for i in range(0, n+2)]
    for l in lost:  # n
        lost_dict[l] = True

    spare_dict = [False for i in range(0, n+2)]
    for r in reserve:   # n
        spare_dict[r] = True

    for i in spare_dict:  # n
        if lost_dict[i] is True and spare_dict[i] is True:
            lost_dict[i], spare_dict[i] = False, False
            answer += 1

    # 2) lost학생의 앞뒤 체크
    for i in lost_dict:  # n
        if lost_dict[i]:
            if i != 1 and spare_dict[i-1]:
                spare_dict[i-1] = False
                answer += 1
            elif i != n and spare_dict[i+1]:
                spare_dict[i+1] = False
                answer += 1

    return answer



'''
6/25 3차 시도 - 성공

시도한 풀이:
    - 1차 시도 + 여벌의 체육복을 가져온 학생이 도난 당했을 경우를 추가
        - >> 2개 정답 추가
    - 2차 시도 + 여벌의 체육복 가져온 학생을 우선하여 처리
'''

def solution3(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # 여벌의 체육복을 가져온 학생에 대한 dictionary
    lost_dict = {i: 0 for i in range(1, n+1)}
    for l in lost:
        lost_dict[l] = 1

    available_dict = {i: 0 for i in range(1, n+1)}
    answer = n - len(lost)

    for r in reserve:
        if lost_dict[r] == 1:
            answer += 1
            lost.remove(r)  # 이 부분이 아주 마음에 들지 않음..
        else:
            available_dict[r] = 1

    for l in lost:
        if l != 1 and available_dict[l-1] == 1:
            answer += 1
            available_dict[l-1] = 0
        elif l != n and available_dict[l+1] == 1:
            answer += 1
            available_dict[l+1] = 0

    return answer

'''
6/25 2차 시도 - 12개 중 2개 오답

시도한 풀이:
    - 1차 시도 + 여벌의 체육복을 가져온 학생이 도난 당했을 경우를 추가
        - >> 2개 정답 추가

오류 탐색:
    - 더 앞의 학생이 이미 여벌의 체육복을 가져왔지만, 체육복을 도난당한 학생에게 체육복을 빌려버리는 경우가 생김.
        - >> 우선적으로 여벌을 가져왔으나 도난당한 친구들을 빼주어야 함.


'''

def solution2(n, lost, reserve):
    lost.sort()
    reserve.sort()

    available_dict = {i: 0 for i in range(1, n+1)}
    answer = n - len(lost)
    for r in reserve:
        available_dict[r] = 1

    for l in lost:
        if available_dict[l] == 1:  # added in 2nd trial
            answer += 1
            available_dict[l] = 0
        elif l != 1 and available_dict[l-1] == 1:
            answer += 1
            available_dict[l-1] = 0
        elif l != n and available_dict[l+1] == 1:
            answer += 1
            available_dict[l+1] = 0

    return answer


'''
6/24 1차 시도 - 12개 중 4개 오답.

시도한 풀이:
    체육복을 추가로 가져온 학생(reserve)을 dictionary를 이용해 표시하고,
    체육복을 잃어버린 학생(lost)로 for loop을 돌며
        1) 해당 학생보다 앞의 학생이 체육복 여벌 가져왔는지 check
        2) 해당 학생 다음의 학생이 체육복 여벌 가져왔는지 check
        
오류 탐색:
    - 1
        - 1) 앞의 학생이 여벌옷을 가져왔는지 먼저 탐색하고,
        - 2) 뒤의 학생이 여벌옷을 가져왔는지 확인하는 방법에 문제가 있는가 ?
        - >> lost탐색 시 앞의 학생부터 차례대로 검사한다면 문제 없음.
    - 2
        - 예외처리에 문제가 있는가?
        - >> oops!! 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
    
'''

def solution1(n, lost, reserve):
    lost.sort()
    reserve.sort()

    available_dict = {i: 0 for i in range(1, n+1)}
    answer = n - len(lost)
    for r in reserve:
            available_dict[r] = 1
    for l in lost:
        if l != 1 and available_dict[l-1] == 1:
            answer += 1
            available_dict[l-1] = 0
        elif l != n and available_dict[l+1] == 1:
            answer += 1
            available_dict[l+1] = 0

    return answer


def test():
    n, lost, reserve = 10001, [i for i in range(10000, 1, -1) if i % 2 == 1], \
                       [i for i in range(10000, 1, -1) if i % 2 == 0]

    start = datetime.now()
    for i in range(LOOP_COUNTER):
        solution(n, lost, reserve)
    print(datetime.now() - start)

    start = datetime.now()
    for i in range(LOOP_COUNTER):
        solution_benchmark(n, lost, reserve)
    print(datetime.now() - start)



if __name__ == '__main__':
    LOOP_COUNTER = 1
    # n, lost, reserve = 5, [2, 4], [1, 3, 5]  # 5
    # print(solution(n, lost, reserve))

    # n, lost, reserve = 5, [2, 4], [3]  # 4
    # print(solution(n, lost, reserve))

    # n, lost, reserve = 3, [3], [1]  # 2
    # print(solution(n, lost, reserve))

    n, lost, reserve = 3, [1, 2, 3], [1, 2, 3]  # 1
    print(solution(n, lost, reserve))

    # test()






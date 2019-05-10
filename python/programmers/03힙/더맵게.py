import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        answer = 0
    else:
        while(True):
            if len(scoville) < 2:
                answer = -1
                break
            else:
                n = heapq.heappop(scoville)
                m = heapq.heappop(scoville)
                output = n + m * 2
                heapq.heappush(scoville, output)
                answer = answer + 1
                if scoville[0] >= K and output >= K:
                    break

    return answer

'''
2차시도
while문도 안됨.
heap으로 다시 시도
def solution(scoville, K):
    answer = 0

    if min(scoville) >= K:
        answer = 0
    else:
        while(True):
            if len(scoville) < 2:
                answer = -1
                break
            else:
                scoville.sort()
                n = scoville.pop(0)
                m = scoville.pop(0)
                output = n + m * 2
                scoville.append(output)
                answer = answer + 1
                if scoville[0] >= K and output >= K:
                    break

    return answer
'''


'''
1차 시도 
효율성에서 런타임 에러 및 시간초과
재귀 -> for문으로 다시 시도
 
def solution(scoville, K):
    answer = 0
    if min(scoville) >= K:
        answer = 0
    else:
        answer = mix(scoville, answer, K)

    return answer


def mix(scoville, answer, K):
    if len(scoville) < 2:
        answer = -1
        return answer
    else:
        scoville.sort()
        n = scoville.pop(0)
        m = scoville.pop(0)
        output = n + m*2
        scoville.append(output)
        answer = answer + 1
        if scoville[0] < K or output < K:
            answer = mix(scoville, answer, K)
        return answer
'''


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))
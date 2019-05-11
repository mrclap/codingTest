'''
5/8 2차 시도,
max heap을 사용하는 깔끔한 방법에 대해 더 고민해봐야겠다.
-1을 곱하여 할 수 있지만 조금 더 근본적으로 해결 하고 싶다.
'''
import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    candidates = []
    supplies = [-x for x in supplies]
    while stock < k:
        # 현재 stock으로 버틸 수 있는 날 중에 추가로 밀가루 수령이 가능한 날과 그 날의 수량 저장
        for i in range(idx, len(dates)):
            if stock >= dates[i]:
                idx = i + 1
                heapq.heappush(candidates, supplies[i])  # 해당일의 공급 가능 물량을 candidates heap에 추가
            else:
                break

        # stock = stock + heapq._heappop_max(candidates)
        stock = stock + heapq.heappop(candidates) * -1
        answer = answer + 1

    return answer


'''
5/8 1차 시도, 시간초과 다수...

def solution(stock, dates, supplies, k):
    answer = 0
    index = None
    while stock < k:
        for idx, d in enumerate(reversed(dates)):
            if stock >= d:  # 현재 stock으로 버티면서 공급가능한 최대 날짜의 index 저장
                index = len(dates) - idx
                # 해당 날짜까지의 공급 중 가장 많이 공급받을 수 있는 날을 선택하여 공급 받음
                heapified_supplies = list.copy(supplies[:index])
                heapq._heapify_max(heapified_supplies)
                local_max = heapq._heappop_max(heapified_supplies)
                stock = stock + local_max
                answer = answer + 1
                for jdx in range(len(supplies)):
                    if supplies[jdx] == local_max:
                        supplies[jdx] = 0
                break

    return answer
'''

if __name__ == '__main__':
    stock = 4
    dates = [4, 10, 15]
    supplies = [20, 5, 10]
    k = 30

    print(solution(stock, dates, supplies, k))

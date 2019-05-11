import heapq
'''
5월 10일 2차 시도
# 전략2
    전략1이 생각보다 쉽게 처리되지 않아
    (두 개의 max, min heap에서 중복되는 것을 처리하는것으로 간단히 구해지지 않음)
    heap을 계속 바꿔가며 무식하게 해보기로함. 
'''


def solution(operations):
    # Consistent Values
    INSERT = "I"
    DELETE = "D"
    MAX = 1
    MIN = -1

    q = []

    answer = [0, 0]

    # string[0] I 인지 D 인지 구분
    while operations:
        o = operations.pop(0)
        h = o[0]    # Alphabet header ("I" or "D")
        val = int(o[2:])  # 공백 제외하고 2번째 값부터 끝까지
        if h == INSERT:
            heapq.heappush(q, val)
        else:
            if q:
                if val == MIN:
                        heapq.heappop(q)
                else:  # val == MAX:
                        # q = -1 * q  # 반전
                        q = [-x for x in q] # 반전
                        heapq.heapify(q)  # heapify
                        heapq.heappop(q)  # max 꺼냄
                        if q:
                            q = [-x for x in q]  # 반전
                            heapq.heapify(q)
    if q:
        answer[1] = q[0]

        q = [-x for x in q]  # 반전
        heapq.heapify(q)

        answer[0] = -1 * q[0]

    return answer
'''
5월 10일 1차 시도
# 전략1
    2개의 heap을 만들어 max와 min을 따로 관리한다.
    나중에 두개를 비교하여 겹치는 원소들로 output을 만든다

def solution(operations):
    # Consistent Values
    INSERT = "I"
    DELETE = "D"
    MAX = 1
    MIN = -1

    min_heap = []
    max_heap = []   # max_heap 구현을 위해 부호 반전 ( 나중에 반드시 -1 곱해줄 것!)

    answer = []

    # string[0] I 인지 D 인지 구분
    while operations:
        o = operations.pop(0)
        h = o[0]    # Alphabet header ("I" or "D")
        val = int(o[2:])  # 공백 제외하고 2번째 값부터 끝까지
        if h == INSERT:
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -1 * val)  # max_heap 구현을 위해 음수값 붙여줌
        else:
            if val == MIN:
                if min_heap:
                    heapq.heappop(min_heap)
            else: # val == MAX:
                if max_heap:
                    heapq.heappop(max_heap)

    # -1 곱하여 최대값으로 보정
    max_heap = [-1 * x for x in max_heap]

    print(min_heap)
    print(max_heap)

    return answer
'''

if __name__ == '__main__':
    operations = ["I 16", "D 1"]
    # operations = ["I 7","I 5","I -5","D -1"]
    # operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]  # [0,0]
    # operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]  # [ 333, -45]
    print(solution(operations))
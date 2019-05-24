# -*- coding: utf-8 -*-
'''
4/30 1차 시도

'''
def solution(p):
    answer = [0 for x in range(len(p))]
    for idx in range(len(p)-1):
        answer[idx] += 1
        for jdx in range(idx+1, len(p)-1):
            if p[jdx] >= p[idx]:
                answer[idx] += 1
            else:
                break

    return answer

if __name__ == '__main__':
    # prices = [1, 2, 3, 2, 3]
    prices = [1, 1, 1, 1, 1]
    print(solution(prices))

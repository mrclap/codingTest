# -*- coding: utf-8 -*-


def solution(p):
    answer = [x for x in range(len(p)-1, -1, -1)]
    for idx in range(len(p)-1, 0, -1):
        for jdx in range(idx-1, -1, -1):
            if p[jdx] > p[idx]:
                answer[jdx] -= 1

    return answer


if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))

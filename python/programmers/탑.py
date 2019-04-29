# -*- coding: utf-8 -*-
'''
benchmark code


def solution(h):
    ans = [0] * len(h)
    for i in range(len(h)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if h[i] < h[j]:
                ans[i] = j+1
                break
    return ans
'''

'''
4/29 first trial
'''

def solution(heights):
    answer = []
    answer.append(0)

    for idx in range(1, len(heights)):
        for jdx in range(idx-1, -1, -1):  # 현재탑 바로 직전 탑부터 더 큰 탑이있었는지 check
            if heights[jdx] > heights[idx]:
                answer.append(jdx+1)
                break
        if len(answer) - 1 != idx:  # 만약 위에서 추가된 answer가 없으면
            answer.append(0)

    return answer



if __name__ == '__main__':

    heights = [6, 9, 5, 7, 4]
    # heights = [3, 9, 9, 3, 5, 7, 2]
    # heights = [1, 5, 3, 6, 7, 6, 5]
    print(solution(heights))

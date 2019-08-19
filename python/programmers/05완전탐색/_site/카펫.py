'''
문제 설명
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 빨간색으로 칠해져 있고 모서리는 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 빨간색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 빨간색 격자의 수 red가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
빨간색 격자의 수 red는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
'''

'''
6/10 1차 시도

    풀었지만 매우 지저분하다..
    다른 분들의 풀이를 보니 단 5줄에 끝낸다..
    반성하자.
    
    + 갈색 타일역시 여러 layer로 존재할 수 있는줄알았으나, 다른 사람들의 풀이를 보니 가장 마지막 1겹만 가능한 것 같다.    
'''


def solution(b, r):
    red_block_aliquot_half = get_aliquot_list_half(r)
    for idx in range(0, len(red_block_aliquot_half)):
        layer = 1
        red_height = red_block_aliquot_half[idx]
        red_width = int(r / red_height)
        no_of_brown_block = brown_block_calculator(red_width, red_height, layer)

        if b == no_of_brown_block:
            return [red_width + 2 * layer, red_height + 2 * layer]
        elif b > no_of_brown_block:
            idx -= 1
            layer += 1

    return [0, 0]


def brown_block_calculator(red_width, red_height, layer):
    return (red_width + (2 * layer) + red_height + (2 * layer)) * 2 - 4


def get_aliquot_list_half(n):
    aliquot_set = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            aliquot_set.add(i)
    aliquot_list = list(aliquot_set)
    aliquot_list.sort()
    return aliquot_list


if __name__ == '__main__':
    # brown = 10
    # red = 2     # [4, 3]

    # brown = 8
    # red = 1   # [3, 3]

    brown = 24
    red = 24  # [8, 6]

    print(solution(brown, red))
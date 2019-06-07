'''
문제 설명
숫자 야구 게임이란 2명이 서로가 생각한 숫자를 맞추는 게임입니다. 게임해보기

각자 서로 다른 1~9까지 3자리 임의의 숫자를 정한 뒤 서로에게 3자리의 숫자를 불러서 결과를 확인합니다. 그리고 그 결과를 토대로 상대가 정한 숫자를 예상한 뒤 맞힙니다.

* 숫자는 맞지만, 위치가 틀렸을 때는 볼
* 숫자와 위치가 모두 맞을 때는 스트라이크
* 숫자와 위치가 모두 틀렸을 때는 아웃
예를 들어, 아래의 경우가 있으면

A : 123
B : 1스트라이크 1볼.
A : 356
B : 1스트라이크 0볼.
A : 327
B : 2스트라이크 0볼.
A : 489
B : 0스트라이크 1볼.
이때 가능한 답은 324와 328 두 가지입니다.

질문한 세 자리의 수, 스트라이크의 수, 볼의 수를 담은 2차원 배열 baseball이 매개변수로 주어질 때, 가능한 답의 개수를 return 하도록 solution 함수를 작성해주세요.
'''

CONSTANT = dict()
CONSTANT['size'] = 3

def solution(baseball):
    answer = 0

    NUMBER_SET = [x for x in range(1, 10)]

    # CANDIDATES_SET =

    IDX_TRIAL = 0
    IDX_STRIKE = 1
    IDX_BALL = 2

    while(baseball):
        this_turn = baseball.pop(0)

        trial = this_turn[IDX_TRIAL]
        strike = this_turn[IDX_STRIKE]
        ball = this_turn[IDX_BALL]



    return answer


def baseball_number_set_maker():
    NUMBERS = [x for x in range(1, 10)]
    number_set = list()
    str = ''
    attaching_number(str, NUMBERS, number_set)

    return number_set


def attaching_number(making, number_remain, number_set):

    if len(making) == CONSTANT['size']:
        number_set.append(int(making))
        return
    else:
        for idx in range(0, len(number_remain)):
            new_making = making + str(number_remain[idx])
            new_number_remain = number_remain.copy()
            del new_number_remain[idx]
            attaching_number(new_making, new_number_remain, number_set)


if __name__ == '__main__':
    baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]  # 2
    baseball_number_set_maker()
    print(solution(baseball))
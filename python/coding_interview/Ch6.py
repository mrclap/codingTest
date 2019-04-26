'''
에라토스테네스의 체
소수만 남기는 func
'''
import math
import time


def sifter_modified(check_range):
    is_prime_num = {i:True for i in range(2, check_range + 1)}
    sqrt_root_of_target = math.floor(math.sqrt(check_range))

    for i in range(2, sqrt_root_of_target + 1):
        if is_prime_num[i] is True:
            for j in range(i*i, check_range + 1, i):  # there is no dividing operation
                is_prime_num[j] = False

    print([i for i in is_prime_num if is_prime_num[i] is True])


def sifter(check_range):
    candidate_list = [i for i in range(2, check_range + 1)]

    for idx, candidate in enumerate(candidate_list):  # N
        candidate_list_compare = list.copy(candidate_list)  # N : Takes too much time
        candidate_list_compare.pop(idx)  # constant
        for candidate_compare in candidate_list_compare: # N
            if candidate_compare % candidate == 0:
                candidate_list.remove(candidate_compare) # N

    print(candidate_list)


if __name__ == '__main__':
    start = time.time()
    sifter(100000)
    print(time.time()-start)

    start = time.time()
    sifter_modified(100000)
    print(time.time() - start)


'''
6.1 무거운 알약
약병 20개가 있다. 이 중 19개에는 1.0그램짜리 알약들이 들어있고, 하나에는 1.1그램짜리 알약들이 들어 있다.
정확한 저울 하나가 주어졌을 때, 무거운 약병을 찾으려면 어떻게 해야 할까? 저울은 딱 한 번만 쓸 수 있다.


'''



'''
6.2 농구
농구 골대가 하나 있는데 다음 두 게임 중 하나를 해 볼 수 있다.
게임1. 슛을 한 번 쏴서 골대에 넣어야 한다.
게임2. 슛을 세 번 쏴서 두 번 골대에 넣어야 한다.
슛을 넣을 확률이 p라고 했을 때 p가 어떤 값일 때 첫 번째 게임을, 혹은 두 번째 게임을 선택하겠는가?

p vs [ 3*p*p*(1-p) + p*p*p ]

p < 0.5 면 게임1 선택
p = 0.5 면 whatever
p > 0.5 면 게임2 선택 
'''




'''
6.3 도미노
8X8 크기의 체스판이 있는데, 대각선 반대 방향 끝에 있는 셀(cell)이 두 개나 떨어져 나갔다.
하나의 도미노로 정확히 두개의 정사각형을 덮을 수 있을 때, 31개의 도미노로 보드 전체를 덮을 수 있겠는가?
여러분의 답이 옳다는 것을 증명하라(예를 들거나, 왜 불가능한지를 보이면 된다).


'''
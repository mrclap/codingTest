import math

def solution():
    n = int(input())
    answer_arr = list()
    for i in range(n):
        answer = 0
        each_line = input()
        input_arr = each_line.split()
        [x1,y1,r1,x2,y2,r2] = map(lambda x:int(x), input_arr)


        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        # case1 두 터렛의 위치가 같고
        if distance == 0:
            # case1.1 관측 거리가 같을 경우 => 무한대
            if r1 == r2: answer = -1
            # case1.2 관측 거리가 다를 경우 => 없음
            else : answer = 0

        # case2 두 터렛의 위치가 다르고
        else :
            # case2.1 외접
            if distance > max(r1, r2):
                # 두 터렛의 거리가 관측거리의 합과 같다면 => 1개
                if distance == r1 + r2:
                    answer = 1
                # 두 터렛의 거리가 관측거리가 합보다 작다면 => 2개
                elif distance < r1 + r2:
                    answer = 2
                # 두 터렛의 거리가 관측거리가 합보다 크다면 => 0개
                else:
                    answer = 0
            # case2.2 내접
            else:
                minR = min(r1, r2)
                maxR = max(r1, r2)
                # 두 터렛의 거리 + 작은원의 관측거리 > 큰원의 관측 거리 => 2개
                if distance + minR > maxR:
                    answer = 2
                # 두 터렛의 거리 + 작은원의 관측거리 = 큰원의 간측 거리 => 1개
                elif distance + minR == maxR:
                    answer = 1
                # 두 터렛의 거리 + 작은원의 관측거리 < 큰원의 관츠 거리 => 0개
                else:
                    answer = 0

        answer_arr.append(answer)

    for answer in answer_arr:
        print(answer)


if __name__ == '__main__':
    solution()


'''
흥미로운 풀이 : 크기 비교 대신 sort 이용해서 케이스를 나눔

import sys
n = int(input())
for i in range(n):
    x1, y1, r1, x2, y2, r2 = list(map(int, sys.stdin.readline().split()))
    dis = ((x2-x1)**2+(y2-y1)**2)**0.5
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    a = [dis, r1, r2]
    a.sort()
    if a[2] > a[0] + a[1]:
        print(0)
    elif a[2] == a[0]+a[1]:
        print(1)
    else:
        print(2)
        

'''
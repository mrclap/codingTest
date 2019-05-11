'''

1       2       3

   (-6)(-7)(-8)

4  (-9) 5 (-11) 6

 (-12)(-13)(-14)

7       8       9
'''

def solution(pattern):
    answer = []
    graph = []
    for idx in range(1, len(pattern)):
        arr = [pattern[idx-1], pattern[idx]]
        graph.append(arr)

    # 두 점을 이은 선이므로 편의를 위해 각 두 점에 대해 오름차순 정렬
    for e in graph:
        e.sort()

    # 1-3 => 1-2-3, 1-7 => 1-5-7 ....
    for idx, e in enumerate(graph):
        if e[0] == 1:
            if e[1] == 3:
                graph[idx] = [1,2,3]
            elif e[1] == 7:
                graph[idx] = [1,5,7]
            elif e[1] == 9:
                graph[idx] = [1,3,8]
        elif e[0] == 2:
            if e[1] == 8:
                graph[idx] = [2,5,8]
        elif e[0] == 3:
            if e[1] == 7:
                graph[idx] = [3,5,7]
            elif e[1] == 9:
                graph[idx] = [3,6,9]
        elif e[0] == 4:
            if e[1] == 6:
                graph[idx] = [4,5,6]

    for idx, e in enumerate(graph):
        if e[0] == 1:
            if e[1] not in [2, 4]:
                pass


    print(graph)

    return answer

if __name__ == '__main__':
    # pattern = [1,2,5,9,8]
    # pattern = [1, 6, 8, 3, 4]
    # pattern = [2, 5, 1, 3]
    pattern = [6, 5, 7, 3, 9]
    # pattern = [5, 3]
    print(solution(pattern))


# def solution(N):
#     answer = []
#     dfs("", 0, N*2, answer)
#
#     answer.sort()
#
#     return answer
#
#
# def dfs(str, status, remain, answer):
#     if remain != 0:
#         if status > 0:
#             if remain > status:
#                 remain -= 1
#                 dfs(str + ')', status - 1, remain, answer)
#                 dfs(str + '(', status + 1, remain, answer)
#             else:
#                 remain -= 1
#                 dfs(str + ')', status - 1, remain, answer)
#         else:
#             remain -= 1
#             dfs(str + '(', status + 1, remain, answer)
#     else:
#         answer.append(str)
#
#
#
#
# if __name__ == '__main__':
#     N = 2
#     # N = 3
#     print(solution(N))

# def solution1(s):
#     answer = 0
#     dic = dict()
#
#     for each in s:
#         current = dic.get(each)
#         if current:
#             dic[each] = current + 1
#         else:
#             dic[each] = 1
#
#     # 2명, 2명 맵핑
#         # 2명 그룹이 짝수이면
#     if dic[2] % 2 == 0:
#         answer += dic[2] / 2
#         dic[2] = 0
#     else:
#         answer += int(dic[2] / 2)
#         dic[2] = 1
#
#     # 1명 + 1명 + 1명 + 1명
#         # 1명 그룹이 4의 배수이면
#     if dic[1] % 4 == 0:
#         answer += dic[1] / 4
#         dic[1] = 0
#         # 1명 그룹이 4의 배수가 아니면
#     else:
#         temp = dic[1]
#         dic[1] = temp % 4
#         answer += int(temp / 4)
#
#         # 1명 그룹의 남은 사람이 3명
#         if dic[1] == 3:
#             answer += 1
#             dic[0] = 0
#
#         # 1명 그룹의 남은 사람이 2명
#         elif dic[1] == 2:
#             if dic[3] >= 1:
#                 # 1명, 3명 맵핑
#                 # 1명인 그룹이 더 많(거나 같)으면
#                 if dic[1] >= dic[3]:
#                     dic[1] -= dic[3]
#                     answer += dic[3]
#                     dic[3] = 0
#                     # 3명인 그룹이 더 많으면
#                 else:
#                     dic[3] -= dic[1]
#                     answer += dic[1]
#                     dic[1] = 0
#
#             # 2명 그룹있으면
#             if dic[2] >= 1 and dic[1] == 2:
#                 dic[2] -= 1
#                 dic[1] = 0
#                 answer += 1
#             # 2명 그룹없으면
#             elif dic[1] == 2:
#                 answer += 1
#                 dic[1] = 0
#
#         # 1명 그룹의 남은 사람이 1명
#         if dic[1] == 1:
#                # 1명, 3명 맵핑
#                     # 1명인 그룹이 더 많(거나 같)으면
#             if dic[1] >= dic[3]:
#                 dic[1] -= dic[3]
#                 answer += dic[3]
#                 dic[3] = 0
#                     # 3명인 그룹이 더 많으면
#             else:
#                 dic[3] -= dic[1]
#                 answer += dic[1]
#                 dic[1] = 0
#
#     for each in dic:
#         if dic[each] != 0:
#             answer += dic[each]
#
#     return answer
#
# if __name__ == '__main__':
#     # s = [1,2,4,3,3] # 4
#     s = [2,3,4,4,2,1,3,1]   # 5
#     print(solution1(s))

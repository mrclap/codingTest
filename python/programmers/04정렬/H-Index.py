'''
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h가 이 과학자의 H-Index입니다.
어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
입출력 예
citations	return
[3, 0, 6, 1, 5]	3
6 5 3 1 0
'''

'''
5/24 다른 사람이 푼 답
    1. enumerate의 사용을 자제해야겠다.
        - 어짜피 index로 접근이 가능하다.
        
    2. for문을 통한 list 접근 방식에 따라 if만 사용할 수도, if/elif를 사용할 수도 있다.
        - 기왕이면 if 한 케이스로 처리하는게 깔끔하지 않을까?
 
'''
def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
'''
5/24 2차 맞음
'''
def solution2(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx+1 == citation:
            answer = idx+1
            break
        elif idx+1 > citation:
            answer = idx
            break
        answer = len(citations)

    return answer

'''
5/24 1차 16케이스 중 1개 틀림
'''
def solution1(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx+1 == citation:
            answer = idx+1
            break
        elif idx+1 > citation:
            answer = idx
            break

    return answer


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    print(solution(citations), '3')

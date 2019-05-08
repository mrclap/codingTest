import heapq

def solution(stock, dates, supplies, k):
    answer = 0

    # while stock < k:
    for d in reversed(dates):
        print(d)

    return answer

if __name__ == '__main__':
    stock = 4
    dates = [4, 10, 15]
    supplies = [20, 5, 10]
    k = 30

    print(solution(stock, dates, supplies, k))

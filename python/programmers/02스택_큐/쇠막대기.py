def solution(arrangement):
    stack = list()
    previous = ''
    target_stick = 0
    cut_stick = 0

    for i in arrangement:
        if i != ')':
            stack.append(i)
            target_stick += 1

        # i == ')':
        elif i == ')' and previous == '(':
            # 레이져
            target_stick -= 1
            stack.pop()
            cut_stick += target_stick
        else:
            target_stick -= 1
            cut_stick += 1
        previous = i

    answer = cut_stick
    return answer


if __name__ == '__main__':
    arrangement = '()(((()())(())()))(())'
    print(solution(arrangement=arrangement))


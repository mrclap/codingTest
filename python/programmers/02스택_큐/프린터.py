def solution(priorities, location):
    answer = 0
    output_arr = list()

    cursor = location
    loop_counter = 0

    attention = False

    while len(priorities):
        current_max = priorities[0]
        for i in range(1, len(priorities)):
            if priorities[i] > current_max:
                current_max = priorities[i]
        candidate = priorities.pop(0)
        if cursor == 0:
            attention = True

        if candidate >= current_max:
            output_arr.append(candidate)
            if attention is True:
                answer = len(output_arr)
                priorities.clear()
            else:
                cursor -= 1
        else:
            priorities.append(candidate)
            if attention is True:
                cursor = len(priorities) - 1
            else:
                cursor -= 1

        attention = False
        loop_counter += 1

    return answer


if __name__ == '__main__':
    # priorities = [2, 1, 3, 2]
    # location = 2
    # print(solution(priorities, location))

    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))
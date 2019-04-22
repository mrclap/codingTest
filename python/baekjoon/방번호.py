import math
from sys import stdin

def get_set_num():
    room_number = stdin.readline()
    num_dict = dict()
    answer = 0
    num_of_six_nine = 0
    for number in room_number:
        if num_dict.get(number):
            num_dict[number] = num_dict.get(number) + 1
        else:
            num_dict[number] = 1

    for each in num_dict:
        if each != '6' and each != '9':
            if answer < num_dict[each]:
                answer = num_dict[each]
        else:
            num_of_six_nine += num_dict[each]

    if answer < math.ceil(num_of_six_nine/2):
        answer = math.ceil(num_of_six_nine/2)
    print(answer)


if __name__ == '__main__':
    get_set_num()

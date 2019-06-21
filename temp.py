from datetime import datetime
import random


'''
    To make order number
    cYYYYMMDDHHmmss##(##)(##)

'''

def get_order_number(item_id, user_id):

    payment_datetime = datetime.now()

    order_number = 'c'

    order_number += str(payment_datetime)[0:4]
    order_number += str(payment_datetime)[5:7]
    order_number += str(payment_datetime)[8:10]
    order_number += str(payment_datetime)[11:13]
    order_number += str(payment_datetime)[14:16]
    order_number += str(payment_datetime)[17:19]

    add_number = random.randrange(0, 100)
    if add_number < 10:
        order_number += "0"
    order_number += str(add_number)

    add_number = int(item_id) % 100
    if add_number < 10:
        order_number += "0"
    order_number += str(add_number)

    add_number = int(user_id) % 100
    if add_number < 10:
        order_number += "0"
    order_number += str(add_number)

    return order_number

def get_order_number2(item_id, user_id):
    two_digit_item_id = "%02d" % (item_id % 100)
    two_digit_user_id = "%02d" % (user_id % 100)
    two_digit_random = "%02d" % random.randrange(0, 100)
    order_number = 'm' + \
                   datetime.now().strftime("%Y%m%d%H%M%S") + \
                   two_digit_random + \
                   two_digit_item_id + \
                   two_digit_user_id
    return order_number


if __name__ == '__main__':
    LOOP_COUNT = 1_000_000  # python3 only

    start = datetime.now()
    for each in range(LOOP_COUNT):
        item_id = random.randrange(0, 100)
        user_id = random.randrange(0, 100)
        get_order_number(item_id, user_id)

    result_1 = datetime.now() - start

    start = datetime.now()
    for each in range(LOOP_COUNT):
        item_id = random.randrange(0, 100)
        user_id = random.randrange(0, 100)
        get_order_number2(item_id, user_id)

    result_2 = datetime.now() - start

    print('get_order_number : ', result_1)
    print('get_order_number2 : ', result_2)

    '''
    1st
    get_order_number :  0:00:26.658614
    get_order_number2 :  0:00:18.540577
    
    2ed
    get_order_number :  0:00:28.163558
    get_order_number2 :  0:00:23.393787

    3rd
    get_order_number :  0:00:27.716771
    get_order_number2 :  0:00:19.986693
    '''


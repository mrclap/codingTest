from datetime import datetime
import random


def get_order_number(user_id, item_id):
    payment_datetime = datetime.now()
    order_number = 'm'

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

    add_number = user_id % 100
    if add_number < 10:
        order_number += "0"
    order_number += str(add_number)

    add_number = item_id % 100
    if add_number < 10:
        order_number += "0"
    order_number += str(add_number)

    return order_number


def get_order_number2(user_id, item_id):
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
    LOOP = 1_000_000
    start = datetime.now()
    for idx in range(LOOP):
        get_order_number(random.randrange(0, 100), random.randrange(0, 100))
    print('get_order_number: ', datetime.now()-start)

    start = datetime.now()
    for idx in range(LOOP):
        get_order_number2(random.randrange(0, 100), random.randrange(0, 100))
    print('get_order_number2: ', datetime.now() - start)

'''
1st 34% faster
    get_order_number:  0:00:18.187910
    get_order_number2:  0:00:12.066294
    
2ed 35% faster
    get_order_number:  0:00:20.052224
    get_order_number2:  0:00:13.042653
'''
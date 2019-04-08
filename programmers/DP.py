import time

# descending
def fibonacci(n):
    global count
    count = count + 1

    if n <= 1:
        return n
    if fib_dict[n] is not False:
        return fib_dict[n]
    fib_dict[n] = fibonacci(n-1) + fibonacci(n-2)
    return fib_dict[n]


# ascending
def fibonacci_asc(n):
    global count_asc

    if fib_dict_asc[n] is False:
        for i in range(n):
            idx = i + 3
            fib_dict_asc[idx] = fib_dict_asc[idx-1] + fib_dict_asc[idx-2]
            count_asc = i + 1

    return fib_dict_asc[n]


if __name__ == '__main__':
    count = 0
    count_asc = 0

    n = 500
    m = 500
    fib_dict = {i+1: False for i in range(n)}
    fib_dict_asc = {i+1: False for i in range(m)}
    fib_dict_asc[1] = 1
    fib_dict_asc[2] = 1

    stime = time.time()
    print(fibonacci(n), count)
    print(time.time() - stime)

    stime = time.time()
    print(fibonacci_asc(m), count_asc)
    print(time.time() - stime)
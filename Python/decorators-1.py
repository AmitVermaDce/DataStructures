import time


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print(f"Time difference: {end - start}")
        return value

    return wrapper


@timed
def myfunc(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result


myfunc(1000)

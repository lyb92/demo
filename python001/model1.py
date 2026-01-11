import time


def decorator(func):
    def wrapper():
        start_time = time.time()
        func()

        end_time = time.time()
        print(end_time - start_time)

    return wrapper


#@decorator
def func():
    time.sleep(8)
func()

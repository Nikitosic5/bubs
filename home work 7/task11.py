from time import time


def decorator(func):
    def wrapper():
        start = time()
        func()
        end= time()
        print(end-start)
    return wrapper

@decorator
def func_to_decor():
    for i in range(1000):
        print(i)
func_to_decor()
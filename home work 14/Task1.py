"""
Напишите декоратор печатающий время выполнения данной функции.
"""
from time import time

# Декоратор пишем тут
def decorate(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(end - start)
        return wrapper()

@decorate
def func_to_decor():
    for i in range(1000):
        print()

func_to_decor()

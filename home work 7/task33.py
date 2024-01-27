def decorate(func):
    def wrapper():
        x = input("Введите число")
        while True:
            if x // 3 == 0:
                print(x // 3)
            elif x == 0:
                func()
                print(x)
    return wrapper

@decorate
def number():
    print("Данная функция выводит все числа между Число А и Число Б сюда подставьте числа что принимает функция")
number()
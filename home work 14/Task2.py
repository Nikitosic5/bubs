"""
Напишите программу добавляющую в рецепт бутерброда ингридиенты "Салат" и "Ананасы" с помощью декораторов.
"""
def decorate(func):
    def wrapper():
        x = input("Введите ингридиент")

        func()
        print(x)
    return wrapper

@decorate
def eat():
    print("Хлеб сыр")
eat()    
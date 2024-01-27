"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""
def calculate_imt(weight, height):
    index = weight / (height * height)
    return index

def process_imt(index):
    if index < 18.5:
        print("Недостаточный вес")
    elif index >= 18.5 and index <= 25:
        print("ИМТ в норме")
    else:
        print("Избыточный вес")

weight = float(input("Введите вес (в кг): "))
height = float(input("Введите рост (в метрах): "))

imt = calculate_imt(weight, height)
process_imt(imt)
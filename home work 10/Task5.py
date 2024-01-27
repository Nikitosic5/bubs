"""
Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.
"""

import sys


def print_colors(colors):
    for color, hex_value in colors.items():
        print(f"Цвет: {color}, HEX: {hex_value}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Недостаточно аргументов!")
    else:
        colors = {}
        num_colors = int(sys.argv[2])
        for i in range(num_colors):
            color = input("Введите название цвета: ")
            hex_value = input("Введите HEX значение: ")
            colors[color] = hex_value

        print_colors(colors)

"""
Напишите генераторное выражения. Для генерации словаря где ключем выступают числа от 0 до 10. А значения эти же числа в 16чной системе счисления.
Работу с 16чной системой найдите в документации Python
"""

decimal_number = int(input("Введите десятичное число: "))
hexadecimal_digits = "012345678910"
hexadecimal_number = ""

while decimal_number > 0:
    remainder = decimal_number
    hexadecimal_digit = hexadecimal_digits[remainder]
    hexadecimal_number = hexadecimal_digit + hexadecimal_number
    decimal_number //= 16

print("Шестнадцатеричное число:", hexadecimal_number)

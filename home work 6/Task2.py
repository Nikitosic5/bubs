"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""
numbers = "0139412831055230677798"
from collections import Counter
def count_it(sequence):
    return dict(Counter([int(num) for num in sequence]). most_common(3))
print(count_it("0139412831055230677798"))


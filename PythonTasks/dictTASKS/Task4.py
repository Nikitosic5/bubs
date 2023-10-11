"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""
from collections import OrderedDict
dct = OrderedDict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last=False)
second = list(dct.items())[1]
del dct[second[0]]
dct['new_key'] = 'new_value'
my_dict =({5: 5, 3: 3, 4: 4, 1: 1, 'new_key': 'new_value'})
id(my_dict)
17128656


"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""


example = "asdasdasqweqwazxczxfgdfg1231245sadfadfsa1231312"
# gen_obj = (i for i in example if i.isalpha())
# for i in gen_obj:
#     print(i)

def gen_func(some):
    for i in some:
        if i.isalpha():
            yield i

gen_object = gen_func(example)
for i in gen_object:
    print(i)
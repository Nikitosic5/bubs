"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""

def cacluate(*args):
    sum(args)
    ave=sum(args)/len(args)
    list=[]
    for i in args:
        if i>ave :
            list.append(i)
    return (ave,list)
print(cacluate(1,2,3,4,5,6))
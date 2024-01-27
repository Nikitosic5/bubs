stoimost = int(input('Введите стоимость покупок:'))
while stoimost > 0:
    if stoimost > 0:
        print(stoimost * 0.9)
        stoimost = int(input('Введите стоимость покупок:'))
    if stoimost == 0:
        print('Конец')
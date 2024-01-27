def products(price):
    p = [k for k, v in {'Попробуйте нашу выпечку':range(1,100), 'Как насчет орехов в шоколаде?':range(100,500)}.items() if price in v]
    return ''.join(p) if p else 'Попробуйте экзотические фрукты'
while True: print(products(int(input('Введите цену: ')))) if input("Введите категорию товара: ") == 'Продукты' else print('Загляните в товары для дома!')
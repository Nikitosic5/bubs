price1 = int(input("Цена первого товара:"))
price2 = int(input("Цена второго товара:"))
price3 = int(input("Цена третьего товара:"))
if price1 <= price2 and price2 <= price3:
    print("Акция")
    print("К оплате:",(price1 + price2 + price3)/2)
elif price3 <= price2 and price2 <= 1:
    print("Акция")
    print("К оплате:", (price1 + price2 + price3) / 3)
else:
    print("К оплате:", (price1 + price2 + price3))
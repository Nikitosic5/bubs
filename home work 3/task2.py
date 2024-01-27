total = int(input('Сумма:'))
time = int(input('Текущее время (час):'))
if time >= 10 and time <= 12:
   total = total/2
   print('Акция! Итого к оплате:', total)
if time >= 20 and time <= 22:
   total = total/4
   print('Акция! Итого к оплате:', total)
if time > 8 and time < 10 or time > 12 and time < 20:
   print('Итого к оплате:', total)
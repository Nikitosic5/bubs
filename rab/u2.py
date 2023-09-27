import re
for c in re.findall(r'[=?*^$№@_]', input('Введите логин:\n')):
  print('Запрещённый символ:', c)